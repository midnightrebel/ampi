from django.db import models

from ampi.ampi.users.models import User


# def owner(self=None):
#     name_owner = User.objects.filter(username=self.request.user)
#     return name_owner


class File(models.Model):
    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    name = models.CharField(max_length=512)
    file = models.FileField(upload_to='files/')
    owner = models.CharField(max_length=512)
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )

    def __str__(self):
        return self.name
