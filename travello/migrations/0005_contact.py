# Generated by Django 5.0.4 on 2024-05-17 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.TextField()),
                ('message', models.TextField()),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
    ]
