# Generated by Django 3.2.13 on 2023-09-06 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cantoras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('instrumento', models.CharField(max_length=30)),
                ('debut_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='NanoGames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('release', models.DateField()),
                ('platform', models.CharField(max_length=20)),
            ],
        ),
    ]