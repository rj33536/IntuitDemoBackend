# Generated by Django 5.1.1 on 2024-10-09 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0004_user_unique_upper_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='events',
            field=models.TextField(default='[]'),
        ),
    ]