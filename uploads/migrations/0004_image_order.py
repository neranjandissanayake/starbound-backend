# Generated by Django 5.0.6 on 2024-09-28 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0003_remove_image_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
