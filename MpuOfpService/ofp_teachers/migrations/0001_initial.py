# Generated by Django 2.2.14 on 2020-07-24 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('GeneralPhysicalTraining', '0002_gymnasium_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=150, verbose_name='ФИО студента')),
                ('attendance_date', models.DateField(verbose_name='Дата посещения')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GeneralPhysicalTraining.Gymnasium', verbose_name='Зал')),
            ],
            options={
                'verbose_name': 'Посещение',
                'verbose_name_plural': 'Посещения',
            },
        ),
    ]
