# Generated by Django 4.1 on 2022-11-28 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='services-img')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]
