# Generated by Django 4.2.16 on 2024-11-17 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0004_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='jitsi_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
