# Generated by Django 5.0.7 on 2024-12-12 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0004_blog_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMSLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('recipients', models.TextField()),
                ('status', models.CharField(max_length=20)),
                ('response', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
