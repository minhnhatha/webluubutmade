from django.db import models
import os
# Create your models here.
def up_name(instance, filename):
    return f'{instance.folder.name}/{filename}'
class Folder(models.Model):
    """
    大好き💕
    """
    user = models.CharField(default="", max_length=25)
    name = models.CharField(default="", max_length=100)
    color = models.CharField(max_length=7, default="#F4D03F")
    note = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=False)
    
    def __str__(self):
        return f'({self.id}) {self.name}'
class File(models.Model):
    """
    🎵我们不一样🎵
    """
    name = models.CharField(default="", max_length=100)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to=up_name)
    index = models.IntegerField(default=1)
    # password = models.CharField(default = "", max_length=50)
    def __str__(self):
        return f'({self.id}) {self.name}({self.index})'
    def get_extension(self):
        return os.path.splitext(self.file.name)[1].lower().lstrip('.')
