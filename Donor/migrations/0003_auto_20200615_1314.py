# Generated by Django 3.0.5 on 2020-06-15 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0002_auto_20200615_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='date_of_birth',
            field=models.DateField(verbose_name='Date'),
        ),
    ]
