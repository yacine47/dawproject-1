# Generated by Django 5.0 on 2023-12-23 08:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='Users.user')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='Users.user')),
            ],
            options={
                'ordering': ['-date_sent'],
            },
        ),
    ]
