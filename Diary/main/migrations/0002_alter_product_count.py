# Generated by Django 5.0.1 on 2024-01-29 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.IntegerField(default=0, verbose_name='Кол-во приготовления блюда'),
        ),
    ]
