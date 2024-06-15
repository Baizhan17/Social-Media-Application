# Generated by Django 5.0.6 on 2024-05-29 21:30

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('sent', 'sent'), ('accept', 'accept'), ('reject', 'reject')], default='sent', max_length=20)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='make_friendrequests', to=settings.AUTH_USER_MODEL)),
                ('request_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_friendrequests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
