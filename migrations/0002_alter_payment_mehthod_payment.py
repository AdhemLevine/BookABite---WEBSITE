# Generated by Django 4.2.7 on 2023-12-01 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='mehthod_payment',
            field=models.CharField(max_length=20),
        ),
    ]
