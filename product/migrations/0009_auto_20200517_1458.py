# Generated by Django 3.0.4 on 2020-05-17 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20200517_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Color')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Size')),
            ],
        ),
        migrations.DeleteModel(
            name='Variations',
        ),
    ]
