# Generated by Django 4.0.5 on 2022-06-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_auto_20220622_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pass_in_trip',
            name='place',
            field=models.PositiveIntegerField(help_text='Введите номер места', unique=True, verbose_name='Номер места'),
        ),
        migrations.AlterField(
            model_name='plane',
            name='capacity',
            field=models.PositiveIntegerField(help_text='Введите кол-во мест в самолете', verbose_name='Количество мест'),
        ),
        migrations.AlterField(
            model_name='plane',
            name='number',
            field=models.PositiveIntegerField(help_text='Введите номер самолета', verbose_name='Номер самолета'),
        ),
    ]
