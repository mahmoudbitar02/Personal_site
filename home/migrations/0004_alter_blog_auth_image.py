# Generated by Django 5.0 on 2024-01-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_blog_auth_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='auth_image',
            field=models.ImageField(upload_to='auth/'),
        ),
    ]