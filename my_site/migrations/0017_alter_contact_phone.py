# Generated by Django 4.1 on 2023-06-22 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0016_category_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
