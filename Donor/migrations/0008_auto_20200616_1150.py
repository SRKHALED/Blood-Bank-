# Generated by Django 3.0.5 on 2020-06-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0007_auto_20200615_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='height',
        ),
        migrations.AddField(
            model_name='donor',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
