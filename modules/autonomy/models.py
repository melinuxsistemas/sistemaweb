from django.db import models


class Autonomy ():
    access_level = (
        ("0", "Sem Acesso"),
        ("1", "vizualizar"),
        ("2", "adicionar"),
        ("3", "alterar"),
        #... Ainda possui mais
    )

    id_access  = models.IntegerField(name="id_access",db_index=True,unique=True)
    id_company = models.CharField(name="id_company")
    id_user = models.CharField(name="id_user")
    menu_01 = models.CharField(name="menu_01",choices=access_level,max_length=15,null=True)
    menu_02 = models.CharField(name="menu_02",choices=access_level,max_length=15,null=True)
    menu_03 = models.CharField(name="menu_03",choices=access_level,max_length=15,null=True)
    menu_04 = models.CharField(name="menu_04",choices=access_level,max_length=15,null=True)
    menu_05 = models.CharField(name="menu_05",choices=access_level,max_length=15,null=True)
    menu_06 = models.CharField(name="menu_06",choices=access_level,max_length=15,null=True)
    menu_07 = models.CharField(name="menu_07",choices=access_level,max_length=15,null=True)
    menu_08 = models.CharField(name="menu_08",choices=access_level,max_length=15,null=True)
    menu_09 = models.CharField(name="menu_09",choices=access_level,max_length=15,null=True)
    comments = models.TextField(name="Observacoes")