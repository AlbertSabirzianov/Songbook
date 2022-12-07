from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from one.models import Song, Part
from .forms import SongForm, PartForm, SongSearchForm
from .Albert import Post, World


def run(request):  # Быстрый поиск
    songs = Song.objects.order_by('name').filter(Q(name__icontains=request.GET.get('q')) | Q(wrigth__icontains=request.GET.get('q')))
    count = len(songs)
    paginator = Paginator(songs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'run.html', {'songs': page_obj, 'count': count, 'q': request.GET.get('q')})


def page(request):  # Новинки!
    return render(request, 'index.html', {'songs': Song.objects.all().order_by('-time')[:3]})


def mane_up(request):  # Главная страница
    count = len(Song.objects.all())
    word = World(count).wr()
    return render(request, 'mane_up.html', {'count': count, 'word': word})


def add(request):  # Страница добавления песни
    if request.method == 'POST':
        form = SongForm(request.POST)
        formparts = PartForm()
        files = request.FILES.getlist('part')
        if form.is_valid() and files:
            f = form.save()
            Post(name=request.POST.get('transcription'), count=len(Song.objects.all()),
                 comp=request.POST.get('name')).send()
            for i in files:
                Part.objects.create(part=i, comp=f)
            count = len(Song.objects.filter(transcription=request.POST.get('transcription')))
            return render(request, 'alldone.html', {'person': request.POST.get('transcription'), 'count': count})
    else:
        form = SongForm()
        formparts = PartForm()
    return render(request, 'add.html', {'form': form, 'formpart': formparts})


def download(request, key):  # Страница скачивания нот песни
    p = Part.objects.all().filter(comp=key)
    song = Song.objects.get(pk=key)
    return render(request, 'download.html', {'parts': p, 'song': song})


def search(request):
    if request.GET.get('have_score'):
        if int(request.GET.get('band1')) == 0 and int(request.GET.get('style1')) == 0:
            search_songs = Song.objects.order_by('name').filter(name__icontains=request.GET['name'],
                                                                wrigth__icontains=request.GET['wrigth'],
                                                                transcription__icontains=request.GET['transcription'],
                                                                have_score=True
                                                                )
        if int(request.GET.get('band1')) > 0 and int(request.GET.get('style1')) == 0:
            search_songs = Song.objects.order_by('name').filter(name__icontains=request.GET['name'],
                                                                wrigth__icontains=request.GET['wrigth'],
                                                                transcription__icontains=request.GET['transcription'],
                                                                have_score=True,
                                                                band=request.GET['band1']
                                                                )
        if int(request.GET.get('band1')) == 0 and int(request.GET.get('style1')) > 0:
            search_songs = Song.objects.order_by('name').filter(name__icontains=request.GET['name'],
                                                                wrigth__icontains=request.GET['wrigth'],
                                                                transcription__icontains=request.GET['transcription'],
                                                                have_score=True,
                                                                style=request.GET['style1']
                                                                )
        if int(request.GET.get('band1')) > 0 and int(request.GET.get('style1')) > 0:
            search_songs = Song.objects.order_by('name').filter(name__icontains=request.GET['name'],
                                                                wrigth__icontains=request.GET['wrigth'],
                                                                transcription__icontains=request.GET['transcription'],
                                                                have_score=True,
                                                                style=request.GET['style1'],
                                                                band=request.GET['band1']
                                                                )
    else:
        if int(request.GET.get('band1')) == 0 and int(request.GET.get('style1')) == 0:
            search_songs = Song.objects.order_by('name').filter(name__icontains=request.GET['name'],
                                                                wrigth__icontains=request.GET['wrigth'],
                                                                transcription__icontains=request.GET['transcription'],
                                                                )
        if int(request.GET.get('band1')) > 0 and int(request.GET.get('style1')) == 0:
            search_songs = Song.objects.order_by('name').filter(name__icontains=request.GET['name'],
                                                                wrigth__icontains=request.GET['wrigth'],
                                                                transcription__icontains=request.GET['transcription'],
                                                                band=request.GET['band1']
                                                                )
        if int(request.GET.get('band1')) == 0 and int(request.GET.get('style1')) > 0:
            search_songs = Song.objects.order_by('name').filter(name__icontains=request.GET['name'],
                                                                wrigth__icontains=request.GET['wrigth'],
                                                                transcription__icontains=request.GET['transcription'],
                                                                style=request.GET['style1']
                                                                )
        if int(request.GET.get('band1')) > 0 and int(request.GET.get('style1')) > 0:
            search_songs = Song.objects.order_by('name').filter(name__icontains=request.GET['name'],
                                                                wrigth__icontains=request.GET['wrigth'],
                                                                transcription__icontains=request.GET['transcription'],
                                                                style=request.GET['style1'],
                                                                band=request.GET['band1']
                                                                )
    paginator = Paginator(search_songs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'search.html',
                  {'form': SongSearchForm(request.GET), 'songs': page_obj, 'count': len(search_songs),
                   'n': request.GET.get('name'), 'w': request.GET.get('wrigth'),
                   't': request.GET.get('transcription'), 'h': request.GET.get('have_score'),
                   'b': request.GET.get('band1'), 's': request.GET.get('style1')})


def search_one(request):
    songs = Song.objects.order_by('name')
    paginator = Paginator(songs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'search_one.html', {'form': SongSearchForm(), 'songs': page_obj, 'count': len(songs)})
