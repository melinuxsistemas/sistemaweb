from django.conf.urls import url
from modules.entity.api import EntityAPI


urlpatterns = [
    url(r'register/person/save$', EntityAPI.save_person),
    url(r'register/contact/(?P<id_entity>[^/]+)/',EntityAPI.save_genérico),
    url(r'register/email/(?P<id_entity>[^/]+)/',EntityAPI.save_genérico),
    url(r'load_entities/(?P<id_entity>[^/]+)/(?P<type_class>[^/]+)/',EntityAPI.load_generico),
    url(r'list/contacts/(?P<id_entity>[^/]+)/(?P<type_class>[^/]+)/',EntityAPI.load_generico),
    url(r'list/emails/(?P<id_entity>[^/]+)/(?P<type_class>[^/]+)/',EntityAPI.load_generico),
    url(r'delete/phone/(?P<id>[^/]+)/(?P<type_class>[^/]+)/',EntityAPI.delete_generico),
    url(r'fields/contacts/(?P<id_contact>[^/]+)/',EntityAPI.load_field_contact),
    url(r'update/phone',EntityAPI.update_contact),
    url(r'update/email',EntityAPI.update_email)
    # APIs administrativas
    #url(r'register/delete/(?P<email>[^/]+)/', EntityAPI.register_delete),
]