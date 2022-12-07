from django.db import models
from django.utils.translation import gettext_lazy as _


class Song(models.Model):
    name = models.CharField(_('Название'), max_length=30)
    wrigth = models.CharField(_('Композитор'), max_length=30)
    transcription = models.CharField(_('Автор транскрипции'), max_length=30)
    have_score = models.BooleanField(_('Наличие партитуры'), default=False)
    music = models.CharField(_("Ссылка на музыкальный пример"), max_length=50, unique=False)
    time = models.DateTimeField(auto_now=True)

    data_score = {
        'False': 'Нет', 'True': 'Есть'
    }

    def get_score(self):
        return self.data_score[str(self.have_score)]

    class Band(models.IntegerChoices):
        DUO = 1, _("Дуэт")
        TRIO = 2, _("Трио")
        QARTET = 3, _("Квартет")
        QUNTET = 4, _("Квинтет")
        SEXTET = 5, _("Секстет")
        BAND = 6, _("Big Band")
        ORCESTR = 7, _("Симфо-джаз")
        UNIC = 8, _("Уникальный состав")

    band = models.PositiveSmallIntegerField(_('Состав'), choices=Band.choices, blank=False, default=3)
    data_band = {
        1: 'Дуэт', 2: 'Трио', 3: 'Квартет', 4: 'Квинтет', 5: 'Секстет', 6: 'Big Band', 7: 'Симфо-джаз',
        8: 'Уникальный состав'
    }

    def get_band(self):
        return self.data_band[self.band]

    class Stile(models.IntegerChoices):
        JAZZ = 1, _('Джаз')
        POP = 2, _('Поп')
        KA = 3, _('Кавера')
        AUT = 4, _('Авторская композиция (аранжировка)')
        FILM = 5, _("Музыка из кино")

    style = models.PositiveSmallIntegerField(_('Стиль'), choices=Stile.choices, blank=False, default=1)
    data_style = {
        1: 'Джаз', 2: 'Поп', 3: 'Кавера', 4: 'Авторская композиция (аранжировка)', 5: 'Музыка из кино'
    }

    def get_style(self):
        return self.data_style[self.style]

    def __str__(self):
        return self.name


class Part(models.Model):
    comp = models.ForeignKey(Song, on_delete=models.CASCADE)
    part = models.FileField(_('Ноты'), upload_to='media', null=False, blank=False)

    def __str__(self):
        return str(self.part)[6:]


class SongForSearch(Song):
    class Band(models.IntegerChoices):
        ZERO = 0, _('Состав не выбран')
        DUO = 1, _("Дуэт")
        TRIO = 2, _("Трио")
        QARTET = 3, _("Квартет")
        QUNTET = 4, _("Квинтет")
        SEXTET = 5, _("Секстет")
        BAND = 6, _("Big Band")
        ORCESTR = 7, _("Симфо-джаз")
        UNIC = 8, _("Уникальный состав")

    band1 = models.PositiveSmallIntegerField(_('Состав'), choices=Band.choices, blank=False, default=0)

    class Stile(models.IntegerChoices):
        ZERO = 0, _('Стиль не выбран')
        JAZZ = 1, _('Джаз')
        POP = 2, _('Поп')
        KA = 3, _('Кавера')
        AUT = 4, _('Авторская композиция (аранжировка)')
        FILM = 5, _("Музыка из кино")

    style1 = models.PositiveSmallIntegerField(_('Стиль'), choices=Stile.choices, blank=False, default=0)
