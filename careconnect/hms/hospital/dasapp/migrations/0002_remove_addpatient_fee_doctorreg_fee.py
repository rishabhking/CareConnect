# Generated by Django 5.0.2 on 2024-07-03 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addpatient',
            name='fee',
        ),
        migrations.AddField(
            model_name='doctorreg',
            name='fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
