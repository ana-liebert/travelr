# Generated by Django 4.0.2 on 2022-02-15 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_city_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='main_app.city'),
        ),
    ]