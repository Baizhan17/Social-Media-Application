# Generated by Django 5.0.6 on 2024-07-03 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_postreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='attachments',
        ),
    ]
