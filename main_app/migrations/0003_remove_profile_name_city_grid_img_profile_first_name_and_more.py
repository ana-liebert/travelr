# Generated by Django 4.0.2 on 2022-02-14 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_city_guide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='city',
            name='grid_img',
            field=models.CharField(default='http', max_length=250),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='first name', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='last name', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.CharField(default='http', max_length=500),
        ),
    ]
