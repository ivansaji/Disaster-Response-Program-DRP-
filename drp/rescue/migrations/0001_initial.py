# Generated by Django 2.2.3 on 2019-07-15 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Refugee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('contact', models.IntegerField()),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
                ('location', models.TextField()),
                ('threat_rating', models.IntegerField()),
                ('necessities', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('contact', models.IntegerField()),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]