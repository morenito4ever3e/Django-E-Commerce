# Generated by Django 3.0.4 on 2020-05-17 10:52

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200516_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
