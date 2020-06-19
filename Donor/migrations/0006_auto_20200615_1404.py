# Generated by Django 3.0.5 on 2020-06-15 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0005_auto_20200615_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='blood',
            field=models.CharField(choices=[('Blood Group', ''), ('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-')], max_length=20),
        ),
        migrations.AlterField(
            model_name='donor',
            name='gender',
            field=models.CharField(choices=[('Choos Gender', ''), ('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20),
        ),
    ]