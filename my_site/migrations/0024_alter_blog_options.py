# Generated by Django 4.1 on 2023-06-23 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0023_delete_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-date_posted']},
        ),
    ]
