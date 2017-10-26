from django.conf.urls import url
from modules.entity.api import EntityController, ContactController

urlpatterns = [
    url(r'register/person/save$', EntityController().save_person),
    url(r'list/entities/',EntityController().load),
    #Rotas Contatos
    url(r'register/contact',ContactController().save),
    url(r'delete/phone/(?P<id_contact>[^/]+)',EntityController().delete_tel),
    url(r'update/phone',EntityController().update_tel),
    url(r'list/contacts/(?P<id_entity>[^/]+)/',EntityController().load_tel),
    #Rotas Emails
    url(r'register/email',EntityController.save_email),
    url(r'update/email',EntityController.update_email),
    url(r'list/emails/(?P<id_entity>[^/]+)/',EntityController.load_email),
    url(r'delete/email/(?P<id_email>[^/]+)',EntityController.delete_email),


    #Falta Consertar APIs do Email

    # APIs administrativas
    #url(r'register/delete/(?P<email>[^/]+)/', EntityAPI.register_delete),
]