from django.conf.urls import url
from modules.entity.api import EntityController, ContactController

urlpatterns = [
    url(r'save$', EntityController.save),
    url(r'filter$',EntityController.filter),
    url(r'update$',EntityController.update),
    #Rotas Contatos
    url(r'register/contact',ContactController.save),
    url(r'delete/phone',ContactController.delete_tel),
    url(r'update/phone',ContactController.update_tel),
    url(r'contacts/',ContactController().load_tel),
    #Rotas Emails
    url(r'register/email',ContactController.save_email),
    url(r'update/email',ContactController.update_email),
    url(r'emails/',ContactController().load_email),
    url(r'delete/email',ContactController.delete_email),


    #Falta Consertar APIs do Email

    # APIs administrativas
    #url(r'register/delete/(?P<email>[^/]+)/', EntityAPI.register_delete),
]