# Generated by Django 2.2.3 on 2019-10-26 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0102_auto_20191024_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='gray_html',
            field=models.TextField(blank=True, default=''),
        ),
    ]
