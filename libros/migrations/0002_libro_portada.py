# Generated by Django 5.2 on 2025-04-09 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='portadas/'),
        ),
    ]
