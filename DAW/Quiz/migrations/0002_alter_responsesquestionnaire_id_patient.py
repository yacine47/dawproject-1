# Generated by Django 5.0.1 on 2024-01-03 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0001_initial'),
        ('Users', '0004_alter_user_dateofbirth_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsesquestionnaire',
            name='id_Patient',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.patient'),
        ),
    ]
