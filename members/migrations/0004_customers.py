# Generated by Django 4.2.1 on 2023-05-24 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_ordered_proid_ordered_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerid', models.CharField(max_length=255)),
                ('customerName', models.CharField(max_length=255)),
                ('customerorder', models.CharField(max_length=255)),
            ],
        ),
    ]
