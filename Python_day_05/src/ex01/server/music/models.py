from django.db import models
import mimetypes


# Create your models here.
class Song():
    
    def __init__(self, name):
        self.name: str = name
        self.content_type: str = self.get_content_type()
        self.path: str = 'meida/' + name
    
    def get_content_type(self):
        return mimetypes.guess_type(self.name)[0]