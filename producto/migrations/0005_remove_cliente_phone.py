# Generated by Django 3.1.1 on 2020-11-05 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_delete_productos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='phone',
        ),
    ]
