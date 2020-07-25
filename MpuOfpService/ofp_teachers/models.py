from django.db import models
import GeneralPhysicalTraining
from datetime import date


class Attendance(models.Model):
    # Посещения учеников
    student = models.CharField("ФИО студента", max_length = 150)
    group = models.CharField("Группа", max_length = 7)
    attendance_date = models.DateField("Дата посещения", default = date.today)
    gym = models.ForeignKey(GeneralPhysicalTraining.models.Gymnasium, verbose_name = "Зал", on_delete = models.CASCADE)

    def __str__(self):
        return "{} {} {}".format(
            self.student, self.group, self.attendance_date
            )

    class Meta:
        verbose_name = "Посещение"
        verbose_name_plural = "Посещения"