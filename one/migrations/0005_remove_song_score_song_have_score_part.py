# Generated by Django 4.1.2 on 2022-11-14 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0004_song_music'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='score',
        ),
        migrations.AddField(
            model_name='song',
            name='have_score',
            field=models.BooleanField(default=False, verbose_name='Есть партитура'),
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part', models.FileField(upload_to='media', verbose_name='Ноты')),
                ('comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.song')),
            ],
        ),
    ]
