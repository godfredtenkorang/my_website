# Generated by Django 5.0.7 on 2024-10-11 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0033_blog_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
    ]
