# Generated by Django 4.0.1 on 2022-01-25 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo_customer_action', '0004_remove_actionpath_action_id_action_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='path',
        ),
    ]
