from django.core.exceptions import ValidationError
from modules.core.config import ERRORS_MESSAGES
from django.http import Http404, HttpResponse
from django.db import IntegrityError
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

    def datalist(self, datalist, list_fields=None):
        response_dict = []
        for item in datalist:
            response_data = self.__format_serialized_model(item, list_fields)
            response_dict.append(response_data)
        return response_dict

    def success(self, object, list_fields=None):
        return self.__response_format(True, '', object, list_fields)

    def error(self, exceptions):
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

        if type(exceptions) == dict:
            message_dict = exceptions

        elif isinstance(exceptions,ValidationError):
            try:
                for item in exceptions.error_dict:
                    field = item
                    exception = exceptions.error_dict[field][0]
                    error_code = exception.code
                    value = exception.args[0]
                    if ': ' in value:
                        value = value.split(": ")[1]
                    message_dict[field] = ERRORS_MESSAGES[error_code]#value
            except Exception as error:
                print("ERRO INTERNO: ",error)
                message_dict = error

        elif isinstance(exceptions,IntegrityError):
            params = exceptions.args[0].split(": ")
            field = params[1].split('.')[1]
            value = ERRORS_MESSAGES["unique"]
            message_dict[field] = value

        else:
            print("ERRO! VERIFIQUE A EXCESSAO: ",exceptions, type(exceptions))
            #paramters = exceptions.args[0].split(': ')
            #code_status = exceptions.args[1]
            #field = paramters[0]
            # value = paramters[1]
            #message_dict[field] = ERRORS_MESSAGES[code_status]
            message_dict = exceptions.args[0]
        return message_dict


class Operation:

    response = Response()

    def save(self,request, formulary=None):
        result, form = self.filter_request(request, formulary)
        object = form.get_object()
        if result:
            response_dict = self.execute(object,object.save)
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
        print("Atualizar:")
        result, form = self.filter_request(request, formulary)
        object = form.get_object(int(request.POST['id']))
        response_dict = self.execute(object,object.save)
        return HttpResponse(json.dumps(response_dict))

    def delete(self,model,object_id):
        print("Excluir: ", model, '[', object_id, ']')
        object = model.objects.filter(id=object_id)
        response_dict = self.execute(object, object.delete)
        return HttpResponse(json.dumps(response_dict))

    def disable(self,model,object_id):
        print("Desativar: ",model,'[',object_id,']')
        object = model.objects.get(pk=object_id)
        object.is_active = False
        response_dict = self.execute(object, object.save)
        return HttpResponse(json.dumps(response_dict))
    
    def execute(self,object,action):
        response_dict = {}
        try:
            action()
            response_dict = self.response.success(object)
        except Exception as e:
            response_dict = self.response.error(e)
        return response_dict

    def __get_exceptions(self,object,form):
        """
        Metodo responsavel por tentar capturar erro no formulario e modelo e retornar tudo junto
        """
        try:
            object.full_clean()
        except Exception as exception:
            model_exceptions = exception.message_dict

        full_exceptions = {}
        form_exceptions = form.format_validate_response()
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
        #print("AGORA VEJA COMO FICOU OS ERROS DE FORMULARIO FORMATADOS: ",response_errors)
        return response_errors

    def get_object(self, object_id=None):
        if object_id is not None:
            object = self.model.objects.get(pk=int(object_id))
        else:
            object = self.model()

        print("VEJA O CLEANED DATA: ",self.cleaned_data)
        print("VEJA O CLEANED ERRORS: ", self.errors)

        for attribute in self.data:
            value = self.data[attribute]
            if attribute != 'csrfmiddlewaretoken':
                field = self.fields[attribute]
                value = field.to_python(value)

            print("ATRIBUTO: ", attribute,": ", value)# attribute, " - ", value)
            setattr(object, attribute, value)

        """
        [
        '__class__', '__deepcopy__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
        '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', 
        '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', 
        '__str__', '__subclasshook__', '__weakref__', 'bound_data', 'clean', 'creation_counter', 'default_error_messages', 
        'default_validators', 'disabled', 'empty_values', 'error_messages', 'get_bound_field', 'has_changed', 'help_text', 
        'hidden_widget', 'initial', 'input_formats', 'label', 'label_suffix', 'localize', 'prepare_value', 'required', 
        'run_validators', 'show_hidden_initial', 'strptime', 'to_python', 'validate', 'validators', 'widget', 'widget_attrs'
        ]
        
        
        ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
        '__getitem__', '__gt__', '__hash__', '__html__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', 
        '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
         '__subclasshook__', '__weakref__', '_bound_fields_cache', '_clean_fields', '_clean_form', '_errors', '_html_output',
          '_post_clean', 'add_error', 'add_initial_prefix', 'add_prefix', 'as_p', 'as_table', 'as_ul', 'auto_id', 'base_fields', 
          'changed_data', 'clean', 'cleaned_data', 'data', 'declared_fields', 'default_renderer', 'empty_permitted', 
          'error_class', 'errors', 'field_order', 'fields', 'files', 'format_validate_response', 'full_clean',
           'get_initial_for_field', 'get_object', 'has_changed', 'has_error', 'hidden_fields', 'initial', 'is_bound', 
           'is_multipart', 'is_valid', 'label_suffix', 'media', 'model', 'non_field_errors', 'options_entity_type', 
           'options_status_register', 'order_fields', 'prefix', 'renderer', 'use_required_attribute', 'visible_fields']
        """

        """    
        for attribute, value in [(x, getattr(self, x)) for x in self.data if not x.startswith('_')]:
            print("ATRIBUTO: ",attribute, " - ", value)
            #try:
            #    form_value = self.cleaned_data[attribute]
            #    setattr(object, attribute, form_value)
            #except:
            #    pass
        """
        return object