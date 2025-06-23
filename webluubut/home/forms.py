from django import forms
from .models import *
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['user', 'name', 'color', 'note']
        widgets = {
            'color': forms.TextInput(attrs={'type': 'color', 'id': 'ColorMaker'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Tên hay biệt danh đều ok nha!",}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ví dụ: Giang Lê, nhím,..."}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Viết gì đó đi...", 'id': "editor-content"}),
        }