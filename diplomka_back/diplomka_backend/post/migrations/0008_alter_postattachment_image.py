# Generated by Django 5.0.6 on 2024-06-26 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_postattachment_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postattachment',
            name='image',
            field=models.ImageField(upload_to='post_postattachment'),
        ),
    ]
