# Generated by Django 2.2.4 on 2019-08-19 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_orm_article_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orm_article',
            old_name='image_url',
            new_name='img_url',
        ),
    ]
