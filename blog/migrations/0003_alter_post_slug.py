# Generated by Django 5.1.1 on 2024-09-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_author_options_alter_post_options_post_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True, verbose_name='Slug'),
        ),
    ]
