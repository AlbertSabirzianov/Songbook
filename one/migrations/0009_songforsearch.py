# Generated by Django 4.1.2 on 2022-11-23 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0008_song_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongForSearch',
            fields=[
                ('song_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='one.song')),
                ('band1', models.PositiveSmallIntegerField(choices=[(0, 'Состав не выбран'), (1, 'Дуэт'), (2, 'Трио'), (3, 'Квартет'), (4, 'Квинтет'), (5, 'Секстет'), (6, 'Big Band'), (7, 'Симфо-джаз'), (8, 'Уникальный состав')], default=0, verbose_name='Состав')),
                ('style1', models.PositiveSmallIntegerField(choices=[(0, 'Стиль не выбран'), (1, 'Джаз'), (2, 'Поп'), (3, 'Кавера'), (4, 'Авторская композиция (аранжировка)'), (5, 'Музыка из кино')], default=0, verbose_name='Стиль')),
            ],
            bases=('one.song',),
        ),
    ]
