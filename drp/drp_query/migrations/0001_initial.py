# Generated by Django 2.2.3 on 2019-07-11 10:23

from django.db import migrations, models
import django.db.models.deletion


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
                ('location', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('completed', models.BooleanField()),
                ('attended_by', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('contact', models.IntegerField()),
                ('alloted_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drp_query.Refugee')),
            ],
        ),
    ]
