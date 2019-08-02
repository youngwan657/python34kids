# Generated by Django 2.2.3 on 2019-08-01 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0032_auto_20190801_0112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('badges', models.ManyToManyField(to='list.Badge')),
            ],
        ),
    ]
