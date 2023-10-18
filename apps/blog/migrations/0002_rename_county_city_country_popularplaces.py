# Generated by Django 4.2.5 on 2023-10-11 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='county',
            new_name='country',
        ),
        migrations.CreateModel(
            name='PopularPlaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cities/', verbose_name='Картинка')),
                ('title', models.CharField(max_length=100, verbose_name='Известное')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Контент')),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='Широта')),
                ('lot', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='blog.city', verbose_name='Известное')),
            ],
            options={
                'verbose_name': 'известное',
                'verbose_name_plural': 'известные',
            },
        ),
    ]
