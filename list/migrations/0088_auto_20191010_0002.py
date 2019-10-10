# Generated by Django 2.2.3 on 2019-10-10 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0087_auto_20191008_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='customuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.CustomUser'),
        ),
        migrations.AlterField(
            model_name='userpoint',
            name='customuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.CustomUser'),
        ),
        migrations.AlterField(
            model_name='userpoint',
            name='pointtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.PointType'),
        ),
    ]
