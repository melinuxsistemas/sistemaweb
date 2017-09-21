from django.conf.urls import url
from modules.entity.api import EntityAPI

urlpatterns = [
    url(r'register/person/save$', EntityAPI.save_person),
    url(r'register/phone',EntityAPI.save_number),
    url(r'load_entities/',EntityAPI.load_entities),
    url(r'contacts/(?P<cpf_cnpj>[^/]+)/',EntityAPI.load_contacts),
    url(r'delete/phone/(?P<id_contact>[^/]+)/',EntityAPI.delete_contact),
    # APIs administrativas
    #url(r'register/delete/(?P<email>[^/]+)/', EntityAPI.register_delete),
]