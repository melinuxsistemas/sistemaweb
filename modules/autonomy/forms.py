from django import forms

from modules.entity.models import Entity


class FormAutonomy (forms.Form):
    access_level = (
        ("0", "Sem Acesso"),
        ("1", "vizualizar"),
        ("2", "adicionar"),
        ("3", "alterar"),
        # ... Ainda possui mais
    )

    id_company = forms.CharField(
        label="Empresa",
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'id_company',
                'class': "form-control",
                'ng-model': 'id_company',
                'required': True,
            }
        )
    )

    id_user = forms.ModelChoiceField(
        queryset= Entity.objects.filter(entity_type='PF').values('entity_name'),
        label="Funcionário",
        empty_label='Selecione um funcionário',
        required=True,
        widget=forms.Select(
            attrs={
                'id': 'id_user',
                'class': "form-control",
                'name':'entity_name',
                'ng-model': 'id_user',
                'required': True,
            }
        )
    )


    menu_01 = forms.MultipleChoiceField(
        label="Entidades",
        choices=access_level,
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'id': 'Entidades',
                'class': "form-control",
                'ng-model': 'Entidades',
            }
        )
    )

    menu_02 = forms.MultipleChoiceField(
        label="Menu 02",
        choices=access_level,
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'id': 'menu_02',
                'class': "form-control",
                'ng-model': 'menu_02'
            }
        )
    )