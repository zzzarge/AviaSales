# Generated by Django 4.2.5 on 2023-10-13 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_country_user_about_user_date_of_birth_user_image_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
