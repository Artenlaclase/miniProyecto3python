# Generated by Django 5.1.3 on 2024-11-11 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_smartphone_relase_date_alter_manufacturer_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smartphone',
            old_name='relase_date',
            new_name='release_date',
        ),
    ]
