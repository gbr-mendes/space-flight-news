# Generated by Django 4.0.1 on 2022-01-27 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_article_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='imageUrl',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m'),
        ),
    ]