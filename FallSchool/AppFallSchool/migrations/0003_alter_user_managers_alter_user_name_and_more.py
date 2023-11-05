# Generated by Django 4.2.6 on 2023-11-05 12:27

import AppFallSchool.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFallSchool', '0002_alter_user_name'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', AppFallSchool.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='telegram',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]