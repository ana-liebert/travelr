# Generated by Django 4.0.2 on 2022-02-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_guide_image2_guide_image3_guide_image4_guide_image5_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='image',
            field=models.CharField(default='Required', max_length=200),
        ),
    ]
