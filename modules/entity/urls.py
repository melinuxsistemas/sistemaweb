from django.conf.urls import url
from modules.entity.api import EntityAPI

urlpatterns = [
    url(r'register/person/save$', EntityAPI.save_person),
    url(r'register/phone',EntityAPI.save_number)
    # APIs administrativas
    #url(r'register/delete/(?P<email>[^/]+)/', EntityAPI.register_delete),
]