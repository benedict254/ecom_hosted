# Generated by Django 3.0.7 on 2020-09-30 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20200929_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='addition_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='addition_info')),
                ('description', models.TextField(blank=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Item')),
            ],
        ),
    ]