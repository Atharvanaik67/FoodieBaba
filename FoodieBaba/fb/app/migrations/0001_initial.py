# Generated by Django 4.2 on 2023-04-19 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('category', models.CharField(choices=[('SI', 'South Indian'), ('PU', 'Punjabi'), ('IT', 'Italian'), ('CH', 'Chinese'), ('FR', 'French'), ('JP', 'Japanese')], max_length=2)),
                ('dtype', models.CharField(choices=[('Veg', 'Veg'), ('NonVeg', 'NonVeg')], max_length=10)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
