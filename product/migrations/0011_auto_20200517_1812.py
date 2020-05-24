# Generated by Django 3.0.4 on 2020-05-17 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20200517_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='variation',
            new_name='variant',
        ),
        migrations.AlterField(
            model_name='variants',
            name='image',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='variants',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='variants',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
