# Generated by Django 3.0.8 on 2020-11-28 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analisa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=8)),
                ('token', models.CharField(max_length=255)),
                ('total', models.IntegerField()),
            ],
        ),
    ]
