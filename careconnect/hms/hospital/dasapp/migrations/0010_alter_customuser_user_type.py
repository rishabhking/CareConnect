# Generated by Django 4.2.16 on 2024-11-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0009_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (2, 'doc')], default=1, max_length=50),
        ),
    ]
