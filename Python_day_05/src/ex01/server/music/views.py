from django.shortcuts import render, redirect
import os
from .forms import MusicForm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import Song


def index(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['music']
        song = Song(uploaded_file.name)
        if file_cheeck(song.content_type):
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            messages.info(request, '<h3 style="color: green;">File was successful uploaded!</h3>')
            return redirect('index')
        else:
            messages.error(request, '<h3 style="color: red;">This file extension is not supported.</h3>')
            return redirect('index')
    else:
        if not os.path.exists('./media/'):
            os.mkdir('./media/')
        music_form = MusicForm()
        music_list = [Song(name) for name in sorted(os.listdir('media/'))]
        data = {
            'music_form': music_form,
            'music_list': music_list
        }
        return render(request, 'music/index.html', data)


def file_cheeck(file_type: str) -> bool:
    return file_type and file_type.startswith('audio')