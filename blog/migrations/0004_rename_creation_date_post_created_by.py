# Generated by Django 4.2.7 on 2023-11-24 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creation_date',
            new_name='created_by',
        ),
    ]
