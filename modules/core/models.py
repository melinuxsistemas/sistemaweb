from django.db import models

from modules.core.config import ERRORS_MESSAGES, BaseConfiguration
from modules.entity.models import BaseModel


class EconomicActivity(models.Model):
    activity_code = models.CharField("Código", null=False, blank=False, max_length=4, validators=[],error_messages=ERRORS_MESSAGES)
    activity_name = models.CharField("Atividade Econômica", null=True, blank=False, max_length=64, validators=[], error_messages=ERRORS_MESSAGES)

    class Meta:
        db_table = 'core_economic_activity'
        verbose_name = 'Economic Activity'
        verbose_name_plural = 'Economic Activities'

    def __str__(self):
        return self.activity_code+" - "+self.activity_name

    def create_initial_database(self):
        for item in BaseConfiguration.economic_activity:
            activity = EconomicActivity()
            fields = item.split(" - ")
            activity.activity_code = fields[0]
            activity.activity_name = fields[1]
            activity.save()

class NaturezaJuridica(models.Model):
    natureza_group = models.CharField("Grupo", null=False, blank=False, max_length=3, validators=[], error_messages=ERRORS_MESSAGES)
    natureza_code = models.CharField("Código", null=True, blank=False, max_length=4, validators=[], error_messages=ERRORS_MESSAGES)
    natureza_name = models.CharField("Natureza Jurídica", null=True, blank=False, max_length=64, validators=[], error_messages=ERRORS_MESSAGES)

    class Meta:
        db_table = 'core_natureza_juridica'
        verbose_name = 'Natureza Juridica'
        verbose_name_plural = 'Naturezas Juridicas'

    def __str__(self):
        if self.natureza_code is None:
            return self.natureza_group + ". " + self.natureza_name
        else:
            return self.natureza_code + " - " + self.natureza_name

    def create_initial_database(self):
        for item in BaseConfiguration.natureza_juridica:
            natureza_group = NaturezaJuridica()
            fields_group = item[0].split('. ')
            natureza_group.natureza_group = int(fields_group[0])
            natureza_group.natureza_name = fields_group[1]
            natureza_group.natureza_code = None
            natureza_group.save()

            for subitem in item[1:]:
                natureza = NaturezaJuridica()
                fields = subitem.split(' - ')
                natureza.natureza_group = natureza_group.natureza_group
                natureza.natureza_code = fields[0]
                natureza.natureza_name = fields[1]
                natureza.save()

class MarketSegment(models.Model, BaseModel):
    segment_name = models.CharField("Seguimento de Mercado", null=False, blank=False, max_length=64, validators=[],error_messages=ERRORS_MESSAGES)
    description = models.TextField("Descrição", max_length=500, null=True, blank=True)

    def __unicode__(self):
        return self.segment_name

    def __str__(self):
        return self.segment_name