from django.core.serializers import serialize

def executar_operacao(registro,operacao):
    response_dict = {}
    if operacao == "save":
        metodo_selecionado = registro.save
        menssage_sucesso = "Registro adicionado com Sucesso!"
        menssage_falha = "Erro! Falha na inclusão do registro (\n"

    elif operacao == "delete":
        metodo_selecionado = registro.delete
        menssage_sucesso = "Registro apagado com Sucesso!"
        menssage_falha = "Erro! Falha na exclusão do registro (\n"

    try:
        metodo_selecionado();
        response_dict['success'] = True
        response_dict['message'] = menssage_sucesso
        response_dict['data-object'] = serialize('json',registro)

    except Exception as e:
        response_dict['success'] = False
        response_dict['message'] = menssage_falha+str(e)+")."
        response_dict['data-object'] = None
    return response_dict