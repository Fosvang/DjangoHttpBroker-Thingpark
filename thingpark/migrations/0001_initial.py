# Generated by Django 2.2b1 on 2019-02-20 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datalogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devid', models.CharField(db_index=True, max_length=256, unique=True)),
                ('name', models.CharField(blank=True, max_length=256)),
                ('description', models.CharField(blank=True, max_length=10000)),
                ('activity_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LorawanMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rssi', models.CharField(blank=True, max_length=256)),
                ('received_at', models.DateTimeField(auto_now_add=True)),
                ('datalogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thingpark.Datalogger')),
            ],
        ),
    ]