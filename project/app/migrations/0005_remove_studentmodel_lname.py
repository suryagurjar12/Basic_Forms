# Generated by Django 5.1 on 2024-08-27 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_qureymodel_alter_studentmodel_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmodel',
            name='lname',
        ),
    ]
