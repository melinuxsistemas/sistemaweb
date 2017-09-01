from django.conf.urls import url
from modules.entity.api import EntityAPI

urlpatterns = [
    url(r'register/person/save$', EntityAPI.save_person),
    # APIs administrativas
    #url(r'register/delete/(?P<email>[^/]+)/', EntityAPI.register_delete),
]