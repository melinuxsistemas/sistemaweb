from django.http import request, Http404, HttpResponse
from modules.core.config import ERRORS_MESSAGES
from datetime import date, datetime
from django.core import serializers
from sistemaweb import settings
import json


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


class Response:

    def datalist(self, datalist, list_fields):
        response_dict = []
        for item in datalist:
            response_data = self.__format_serialized_model(item, list_fields)
            response_dict.append(response_data)
        return response_dict

    def success(self, object, list_fields):
        return self.__response_format(True, '', object, list_fields)

    def error(self, exceptions):
        print("VEJA AS EXCESSOES: ",exceptions)
        return self.__response_format(False,self.__format_exceptions(exceptions),None, None)

    def __response_format(self,result, message, obj=None, list_fields=None):
        response_dict = {}
        response_dict['result'] = result
        response_dict['message'] = message
        if result:
            response_dict['object'] = self.__format_serialized_model(obj, list_fields)
        else:
            response_dict['object'] = None
        return response_dict

    def __format_serialized_model(self,object,list_fields):
        if list_fields is not None:
            response_model = serializers.serialize('json', [object], fields=tuple(list_fields))
        else:
            response_model = serializers.serialize('json', [object])

        response_model = json.loads(response_model)[0]
        response_model = response_model['fields']
        response_model['id'] = object.id
        response_model['selected'] = ''
        return response_model

    def __format_exceptions(self,exceptions):
        message_dict = {}
        if type(exceptions) == list:
            for item in exceptions:
                if len(item.args) > 1:
                    status_code = item.args[1]
                    except_parts = str(item).replace("['", "").replace("']", "")
                    if ": " in except_parts:
                        except_parts = except_parts.split(': ')
                        field = except_parts[0]

                    else:
                        field = "Erro! Formato de mensagem nao foi gerado pois o campo do formulario e desconhecido."
                else:
                    if 'UNIQUE' in item.args[0]:
                        status_code = 'unique'

                    except_parts = str(item)
                    if ": " in except_parts:
                        except_parts = except_parts.split(': ')
                        field = except_parts[1].split('.')[1]

                """ 
                Quando temos apenas um erro esse e o formato da excessao:
                   django.core.exceptions.ValidationError: ['cpf_cnpj: Cpf number is not valid.']

                Contudo pode ser que o mesmo campo tenha duas validacoes com erro 
                sendo necessario adequar essa funcao para tratar isso.
                """
                message_dict[field] = ERRORS_MESSAGES[status_code]

        else:
            print("VEJA O QUE TEMOS: ", exceptions, type(exceptions))
            paramters = exceptions.args[0].split(': ')
            code_status = exceptions.args[1]
            field = paramters[0]
            # value = paramters[1]
            message_dict[field] = ERRORS_MESSAGES[code_status]
        return message_dict


class Operation:

    response = Response()

    def save(self,request, formulary):
        result, form = self.filter_request(request, formulary)
        object = form.get_object()
        if result:
            response_dict = self.__execute(object,object.save)
        else:
            response_dict = self.__get_exceptions(object,form)
        return HttpResponse(json.dumps(response_dict))

    def object(self):
        pass

    def filter(self, request, model, queryset=None, order_by="-id",list_fields=None, limit=None):
        result, form = self.filter_request(request)
        if result:
            if queryset is None:
                model_list = model.objects.all().order_by(order_by)
            else:
                model_list = queryset

            if limit is not None:
                model_list = model_list.limit(limit)

            response_dict = self.response.datalist(model_list,list_fields)
            return HttpResponse(json.dumps(response_dict, default=json_serial))
        else:
            raise Http404

    def update(self,request, formulary):
        result, form = self.filter_request(request, formulary)
        object = form.get_object(int(request.POST['id']))
        response_dict = self.__execute(object,object.save)
        return HttpResponse(json.dumps(response_dict))

    def delete(self,model,object_id):
        print("Ja vindo aqui", object_id)
        object = model.objects.filter(id=object_id)
        response_dict = self.__execute(object, object.delete)
        return HttpResponse(json.dumps(response_dict))

    def __execute(self,object,action):
        try:
            action()
            response_dict = self.response.success(object)

        except Exception as e:
            response_dict = self.response.error(object.model_exceptions)
        return response_dict

    def __get_exceptions(self,object,form):
        object.check_validators()
        model_exceptions = self.response.error(object.model_exceptions)
        form_exceptions = form.format_validate_response()

        full_exceptions = {}  # dict(form_exceptions, **model_exceptions);
        full_exceptions.update(model_exceptions)
        full_exceptions.update(form_exceptions)
        return self.response.error(full_exceptions)


class BaseController(Operation, Response):

    def filter_request(self, request, formulary=None):
        if request.is_ajax() or settings.DEBUG:
            if formulary is not None:
                form = formulary(request.POST)
                if form.is_valid():
                    return True, form
                else:
                    return False, form
            else:
                return True, True
        else:
            raise Http404


class BaseForm:

    def format_validate_response(self):
        response_errors = {}
        if self.errors:
            errors = self.errors
            for campo in errors:
                response_errors[campo] = []
                for erro in errors[campo]:
                    erro_format = str(erro)
                    erro_format = erro_format.replace("['", "")
                    erro_format = erro_format.replace("']", "")
                    response_errors[campo].append(erro_format)
        return response_errors

    def get_object(self, object_id=None):
        if object_id is not None:
            object = self.model.objects.get(pk=int(object_id))
        else:
            object = self.model()


        for attribute, value in [(x, getattr(self, x)) for x in self.__dict__ if not x.startswith('_')]:
            try:
                form_value = self.cleaned_data[attribute]
                setattr(object, attribute, form_value)
            except:
                pass
        return object