# Generated by Django 5.2.1 on 2025-06-16 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_rename_categry_contact_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='category',
            new_name='Category',
        ),
    ]
