# Generated by Django 2.2.3 on 2019-08-17 21:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0047_auto_20190816_0035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'ordering': ['-order'], 'verbose_name_plural': 'Quizzes'},
        ),
        migrations.AlterField(
            model_name='quiz',
            name='example',
            field=ckeditor.fields.RichTextField(blank=True, default='<p>Example 1:</p>\n<table border="1" cellpadding="1" cellspacing="1" class="table table-bordered">\n\t<tbody>\n\t\t<tr>\n\t\t\t<td>\n\t\t\t<p><strong>Input</strong>:&nbsp;</p>\n\t\t\t<p><strong>Output</strong>:&nbsp;</p>\n\t\t\t</td>\n\t\t</tr>\n\t</tbody>\n</table>\n<p>&nbsp;</p>\n<p>Example 2:</p>\n<table border="1" cellpadding="1" cellspacing="1" class="table table-bordered">\n\t<tbody>\n\t\t<tr>\n\t\t\t<td>\n\t\t\t<p><strong>Input</strong>:&nbsp;</p>\n\t\t\t<p><strong>Output</strong>:&nbsp;</p>\n\t\t\t</td>\n\t\t</tr>\n\t</tbody>\n</table>\n', null=True),
        ),
    ]
