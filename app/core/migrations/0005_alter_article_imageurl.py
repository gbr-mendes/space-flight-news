# Generated by Django 4.0.1 on 2022-01-27 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_article_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='imageUrl',
            field=models.URLField(blank=True, null=True),
        ),
    ]
