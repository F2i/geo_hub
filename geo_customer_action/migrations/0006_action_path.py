# Generated by Django 4.0.1 on 2022-01-25 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo_customer_action', '0005_remove_action_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='path',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='geo_customer_action.actionpath'),
            preserve_default=False,
        ),
    ]
