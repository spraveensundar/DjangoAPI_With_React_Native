# Generated by Django 5.1.7 on 2025-03-31 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='settings_name', max_length=256)),
                ('value', models.CharField(blank=True, default='', max_length=256)),
            ],
        ),
    ]
