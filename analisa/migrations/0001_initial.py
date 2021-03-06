# Generated by Django 3.0.8 on 2020-11-26 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Antara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
                ('january', models.IntegerField()),
                ('february', models.IntegerField()),
                ('march', models.IntegerField()),
                ('april', models.IntegerField()),
                ('may', models.IntegerField()),
                ('june', models.IntegerField()),
                ('july', models.IntegerField()),
                ('august', models.IntegerField()),
                ('september', models.IntegerField()),
                ('october', models.IntegerField()),
                ('november', models.IntegerField()),
                ('december', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Detik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
                ('january', models.IntegerField()),
                ('february', models.IntegerField()),
                ('march', models.IntegerField()),
                ('april', models.IntegerField()),
                ('may', models.IntegerField()),
                ('june', models.IntegerField()),
                ('july', models.IntegerField()),
                ('august', models.IntegerField()),
                ('september', models.IntegerField()),
                ('october', models.IntegerField()),
                ('november', models.IntegerField()),
                ('december', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kompas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
                ('january', models.IntegerField()),
                ('february', models.IntegerField()),
                ('march', models.IntegerField()),
                ('april', models.IntegerField()),
                ('may', models.IntegerField()),
                ('june', models.IntegerField()),
                ('july', models.IntegerField()),
                ('august', models.IntegerField()),
                ('september', models.IntegerField()),
                ('october', models.IntegerField()),
                ('november', models.IntegerField()),
                ('december', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
    ]
