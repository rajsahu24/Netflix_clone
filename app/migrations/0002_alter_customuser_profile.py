# Generated by Django 4.0.2 on 2022-02-09 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile',
            field=models.ManyToManyField(blank=True, to='app.Profile'),
        ),
    ]
