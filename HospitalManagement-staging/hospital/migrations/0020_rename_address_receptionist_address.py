# Generated by Django 4.0.3 on 2022-04-18 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_receptionist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receptionist',
            old_name='Address',
            new_name='address',
        ),
    ]
