# Generated by Django 3.0.5 on 2020-05-10 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotellu_app', '0003_auto_20200509_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=20, unique=True),
        ),
    ]
