# Generated by Django 3.0.7 on 2020-09-29 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Men', 'Men'), ('Electronics', 'Electronics'), ('Cars', 'Cars'), ('Food', 'Food'), ('Books', 'Books'), ('Shoe', 'Shoe')], max_length=15),
        ),
    ]
