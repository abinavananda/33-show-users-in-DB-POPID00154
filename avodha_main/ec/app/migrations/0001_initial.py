# Generated by Django 5.0.3 on 2024-04-01 01:50

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
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('comopsition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('CR', 'Curd'), ('ML', 'Milk'), ('LS', 'Lassi'), ('MS', 'Milkshake'), ('GH', 'Ghee'), ('PA', 'Paneer'), ('CH', 'Cheese'), ('IC', 'Ice cream')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
