# Generated by Django 4.2.1 on 2023-06-27 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_member_memid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', models.CharField(max_length=255)),
                ('ordername', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
