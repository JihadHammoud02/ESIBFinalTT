# Generated by Django 2.0.7 on 2022-05-01 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='purshace_time',
            new_name='purchase_time',
        ),
    ]
