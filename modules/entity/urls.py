from django.conf.urls import url
from modules.entity.api import EntityAPI


urlpatterns = [
    url(r'register/person/save$', EntityAPI.save_person),
    url(r'list/entities/',EntityAPI.load_entities),
    #Rotas Contatos
    url(r'register/contact',EntityAPI.save_tel),
    url(r'delete/phone/(?P<id_contact>[^/]+)',EntityAPI.delete_tel),
    url(r'update/phone',EntityAPI.update_tel),
    url(r'list/contacts/(?P<id_entity>[^/]+)/',EntityAPI.load_tel),
    #Rotas Emails
    url(r'register/email',EntityAPI.save_email),
    url(r'update/email',EntityAPI.update_email),
    url(r'list/emails/(?P<id_entity>[^/]+)/',EntityAPI.load_email),
    url(r'delete/email/(?P<id_email>[^/]+)',EntityAPI.delete_email),


    #Falta Consertar APIs do Email

    # APIs administrativas
    #url(r'register/delete/(?P<email>[^/]+)/', EntityAPI.register_delete),
]