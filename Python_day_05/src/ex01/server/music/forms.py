from django.forms import forms


class MusicForm(forms.Form):
    music = forms.FileField(label="Upload music")