# Generated by Django 5.0.6 on 2024-06-17 18:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_posts_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends_suggestion',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
