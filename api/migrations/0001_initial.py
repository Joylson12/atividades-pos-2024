# Generated by Django 4.2.7 on 2024-12-20 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('local', models.CharField(max_length=100)),
                ('ano_criacao', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('segundos', models.IntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.artista'),
        ),
    ]