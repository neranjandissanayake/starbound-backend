# Generated by Django 5.0.6 on 2024-10-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_post_is_deleted_remove_product_is_deleted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
