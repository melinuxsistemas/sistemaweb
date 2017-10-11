from django.conf.urls import url
from modules.entity.api import EntityController


urlpatterns = [
    url(r'register/person/save$', EntityController().save_person),
    url(r'register/phone/(?P<id_entity>[^/]+)/',EntityController.save_number),
    url(r'register/email',EntityController.save_email),
    url(r'load_entities/',EntityController().load),
    url(r'list/contacts/(?P<id_entity>[^/]+)/',EntityController.load_contacts),
    url(r'list/emails/(?P<cpf_cnpj>[^/]+)/',EntityController.load_emails),
    url(r'delete/phone/(?P<id_contact>[^/]+)/',EntityController.delete_contact),
    url(r'fields/contacts/(?P<id_contact>[^/]+)/',EntityController.load_contact),
    url(r'update/phone',EntityController.update_contact)
    # APIs administrativas
    #url(r'register/delete/(?P<email>[^/]+)/', EntityAPI.register_delete),
]