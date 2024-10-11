# Generated by Django 5.0.7 on 2024-10-11 19:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0030_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='', upload_to='blog-img')),
                ('content1', models.TextField(blank=True, default='', null=True)),
                ('content2', models.TextField(blank=True, default='', null=True)),
                ('content3', models.TextField(blank=True, default='', null=True)),
                ('content4', models.TextField(blank=True, default='', null=True)),
                ('content5', models.TextField(blank=True, default='', null=True)),
                ('content6', models.TextField(blank=True, default='', null=True)),
                ('content7', models.TextField(blank=True, default='', null=True)),
                ('content8', models.TextField(blank=True, default='', null=True)),
                ('content9', models.TextField(blank=True, default='', null=True)),
                ('content10', models.TextField(blank=True, default='', null=True)),
                ('content11', models.TextField(blank=True, default='', null=True)),
                ('content12', models.TextField(blank=True, default='', null=True)),
                ('content13', models.TextField(blank=True, default='', null=True)),
                ('content14', models.TextField(blank=True, default='', null=True)),
                ('content16', models.TextField(blank=True, default='', null=True)),
                ('content17', models.TextField(blank=True, default='', null=True)),
                ('content18', models.TextField(blank=True, default='', null=True)),
                ('content19', models.TextField(blank=True, default='', null=True)),
                ('content20', models.TextField(blank=True, default='', null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]