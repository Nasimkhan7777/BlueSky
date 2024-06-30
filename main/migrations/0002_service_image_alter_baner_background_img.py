# Generated by Django 5.0.6 on 2024-06-30 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default='default_image.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='baner',
            name='background_img',
            field=models.ImageField(upload_to='media/', verbose_name='Background Image'),
        ),
    ]
