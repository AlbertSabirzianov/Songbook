import json
import os

from art import text2art
from django.core.management import BaseCommand
from django.core.files.base import ContentFile

from one.models import Song, Part


class Command(BaseCommand):
    """Загружаем данные в базу данных."""

    SONGS_PATH = 'songs.json'
    PARTS_PATH = 'parts'

    def push_songs(self):
        """Загружаем в базу данных песни."""

        print('push_songs.....')
        with open(self.SONGS_PATH, 'r', encoding='utf-8') as file:
            songs = json.load(file)

        Song.objects.bulk_create(
            [Song(**song) for song in songs]
        )

    def push_parts(self):
        """Загружаем в базу партии."""

        print('push_parts.....')
        parts = os.listdir(self.PARTS_PATH)

        for part in parts:
            name_of_song = part.split('_')[0]
            with open('parts/' + part, 'rb') as file:
                Part.objects.create(
                    comp=Song.objects.filter(name__icontains=name_of_song)[0],
                    part=ContentFile(file.read(), name=part)
                )

    def handle(self, *args, **options):

        print(text2art('start'))
        self.push_songs()
        self.push_parts()
        print(text2art('success'))
