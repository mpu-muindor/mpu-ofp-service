from django.db import models



class Gymnasium(models.Model):
    # Физкультурные залы
    name = models.CharField("Наименование", max_length = 100)
    address = models.CharField("Адрес", max_length = 100)
    description = models.TextField("Описание", default="Физкультурный зал")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Физкультурный зал"
        verbose_name_plural = "Физкультурные залы"


"""
from django.contrib.auth.models import AbstractUser


class SystemUser(AbstractUser):
    USER_TYPES = (
        ("Student", "Студент"),
        ("Teacher", "Преподаватель"),
        )
    type = models.CharField("Тип пользователя", choices = USER_TYPES, max_length = 7)
"""