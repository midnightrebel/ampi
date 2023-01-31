from django.db import models


class Report(models.Model):
    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'

    id_file = models.IntegerField()
    count_down = models.IntegerField()
