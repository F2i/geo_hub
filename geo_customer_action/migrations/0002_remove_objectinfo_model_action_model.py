# Generated by Django 4.0.1 on 2022-01-25 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('geo_customer_action', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objectinfo',
            name='model',
        ),
        migrations.AddField(
            model_name='action',
            name='model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='contenttypes.contenttype'),
            preserve_default=False,
        ),
    ]
