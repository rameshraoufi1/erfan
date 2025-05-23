# Generated by Django 5.1.7 on 2025-03-27 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erfanian_extraction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_service_name', models.CharField(max_length=100)),
                ('about_service_description', models.TextField(max_length=200)),
                ('about_blog_name', models.CharField(max_length=100)),
                ('about_blog_image', models.ImageField(upload_to='media')),
                ('about_blog_description', models.TextField(max_length=200)),
            ],
        ),
    ]
