# Generated by Django 4.2.10 on 2024-02-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_remove_user_subscriptioncancel'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='current_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]