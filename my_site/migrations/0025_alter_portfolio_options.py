# Generated by Django 4.1 on 2023-08-01 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0024_alter_blog_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ['-title']},
        ),
    ]
