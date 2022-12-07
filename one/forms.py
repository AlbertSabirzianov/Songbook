from django.forms import ModelForm, ClearableFileInput
from .models import Song, Part, SongForSearch


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'


class PartForm(ModelForm):
    class Meta:
        model = Part
        fields = ['part']
        widgets = {
            'part': ClearableFileInput(attrs={'multiple': True})
        }


class SongSearchForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['wrigth'].required = False
        self.fields['transcription'].required = False

    class Meta:
        model = SongForSearch
        fields = ['name', 'wrigth', 'transcription', 'have_score', 'band1', 'style1']

