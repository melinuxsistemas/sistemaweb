from django.conf.urls import url
from modules.entity.api import EntityAPI


urlpatterns = [
    url(r'register/person/save$', EntityAPI.save_person),
    url(r'register/contact/(?P<id_entity>[^/]+)/',EntityAPI.save_tel),
    url(r'delete/phone/(?P<id_contact>[^/]+)',EntityAPI.delete_tel),
    url(r'update/phone',EntityAPI.update_tel),
    url(r'list/contacts/(?P<id_entity>[^/]+)/',EntityAPI.load_tel),

    #Falta Consertar APIs do Email
    url(r'register/email/(?P<id_entity>[^/]+)/',EntityAPI.save_genérico),
    url(r'load_entities/(?P<id_entity>[^/]+)/(?P<type_class>[^/]+)/',EntityAPI.load_generico),
    url(r'list/emails/(?P<id_entity>[^/]+)/(?P<type_class>[^/]+)/',EntityAPI.load_generico),
    url(r'update/email',EntityAPI.update_email)
    # APIs administrativas
    #url(r'register/delete/(?P<email>[^/]+)/', EntityAPI.register_delete),
]