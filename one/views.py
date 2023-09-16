from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from one.models import Song, Part

from .forms import SongForm, PartForm, SongSearchForm
from .utils import World, WordTr
from .filters import SongFilter


def run(request):
    """Страница быстрого поиска."""

    songs = Song.objects.filter(
        Q(name__icontains=request.GET.get('q')) |
        Q(wrigth__icontains=request.GET.get('q'))
    )
    paginator = Paginator(songs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'songs': page_obj,
        'count': songs.count(),
        'q': request.GET.get('q')
    }
    return render(request, 'run.html', context)


def page(request):
    """Страница Новинок."""

    context = {
        'songs': Song.objects.all().order_by('-time')[:3]
    }
    return render(request, 'index.html', context)


def mane_up(request):
    """Главная страница."""

    count = Song.objects.all().count()
    word = World(count).wr()
    context = {
        'count': count,
        'word': word
    }
    return render(request, 'mane_up.html', context)


def add(request):
    """Страница добавления песни."""

    if request.method == 'POST':
        form = SongForm(request.POST)
        files = request.FILES.getlist('part')
        if form.is_valid() and files:
            song = form.save()
            for file in files:
                Part.objects.create(part=file, comp=song)
            count = Song.objects.filter(
                transcription=request.POST.get('transcription')
            ).count()
            context = {
                'person': request.POST.get('transcription'),
                'count': count,
                'word': WordTr(count).wr()
            }
            return render(request, 'alldone.html', context)

        return render(request, 'errors.html', {'errors': form.errors})

    form = SongForm()
    formparts = PartForm()
    return render(request, 'add.html', {'form': form, 'formpart': formparts})


def download(request, key):
    """Страница скачивания нот песни."""

    parts = Part.objects.all().filter(comp=key)
    song = get_object_or_404(Song, pk=key)
    context = {
        'parts': parts,
        'song': song
    }
    return render(request, 'download.html', context)


def search(request):
    """Страница поиска песни."""

    search_songs = SongFilter(request.GET, queryset=Song.objects.all()).qs
    paginator = Paginator(search_songs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'form': SongSearchForm(request.GET),
        'songs': page_obj,
        'count': search_songs.count(),
        'n': request.GET.get('name'),
        'w': request.GET.get('wrigth'),
        't': request.GET.get('transcription'),
        'h': request.GET.get('have_score'),
        'b': request.GET.get('band1'),
        's': request.GET.get('style1')
    }
    return render(request, 'search.html', context)


def search_one(request):
    """
    Первоначальная страница поика, отаброжает
    все песни.
    """

    songs = Song.objects.all()
    paginator = Paginator(songs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'form': SongSearchForm(),
        'songs': page_obj,
        'count': songs.count()
    }
    return render(request, 'search_one.html', context)
