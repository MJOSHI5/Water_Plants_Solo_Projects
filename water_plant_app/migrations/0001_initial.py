# Generated by Django 2.2 on 2021-04-04 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plants', models.CharField(max_length=255)),
                ('day', models.CharField(max_length=140)),
                ('time', models.CharField(max_length=140)),
                ('quantity', models.CharField(max_length=14)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('description', models.TextField()),
                ('finished', models.CharField(max_length=5, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('room', models.CharField(max_length=140, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('favorites', models.ManyToManyField(related_name='user_favorite', to='water_plant_app.User')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plant_owner', to='water_plant_app.User')),
                ('user_likes', models.ManyToManyField(related_name='liked_plant', to='water_plant_app.User')),
            ],
        ),
    ]
