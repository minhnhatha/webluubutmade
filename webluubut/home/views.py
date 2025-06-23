from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from home.models import *
from .forms import *
from django.contrib import messages
import os, base64
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import TooManyFieldsSent, RequestDataTooBig, SuspiciousOperation
# Create your views here.
just_a_little_bit_course = 0
word = ['docx', 'doc', 'dotx', 'dot', 'docm']
excel = ['xlsx', 'xls', 'xlsm', 'xltx', 'xlt', 'xlsb', 'xlam']
powerpoint = ['pptx', 'ppt', 'pptm', 'potx', 'pot', 'ppsx', 'pps']
picture = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp', 'tiff', 'tif', 'svg', 'heif', 'heic', 'cr2', 'nef', 'arw', 'dng']
video = ['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm', 'mpg', 'mpeg', '3gp']
sound = ['mp3', 'wav', 'aac', 'flac', 'ogg', 'wma', 'm4a', 'amr', 'mid', 'midi']
def home(request):
    global just_a_little_bit_course
    just_a_little_bit_course = 0
    use = request.user
    data = {}
    if use.is_authenticated:
        data = {
            'folders': Folder.objects.filter(state=True),
            "use": use,
        }
    return render(request, "home.html", data)
def newhome(request):
    global just_a_little_bit_course
    if request.method == 'POST' and request.POST.get('action') == 'upload':
        folder_form = FolderForm(request.POST)
        # f_form = FolderForm(request.POST)
        # print(f_form)
        files = request.FILES.getlist('files')
        if not len(files):
            messages.error(request, "Bạn chưa chọn file!")
            return redirect("new")
        elif len(files) > 30:
            messages.error(request, "Chọn ít hơn 30 file thôi nha bạn.")
            return redirect("new")
        elif folder_form.is_valid():
            folder = folder_form.save()
            just_a_little_bit_course = folder.id
            # for file in files:
            #     File(name = file.name, folder = folder, file = file).save()
            k = []
            for idx, i in enumerate(files, File.objects.filter(folder=folder).count() + 1):
                f = File(name = f'{i}', folder=folder, file=i, index = idx)
                f.save()
                k.append(f)
            A = []
            C = []
            # file_2 = request.FILES.getlist('files')
            # print(file_2)
            for file in files:
                A.append(os.path.splitext(file.name)[1].lower().lstrip('.'))
                C.append(os.path.splitext(file.name)[0])
            # if request.method == 'POST' and request.POST.get('action') == 'change':
            #     return render(request, 'new.html',
            #     {'pg':True,
            #     'B': zip(C, A),
            #     'word': word,
            #     'excel': excel,
            #     'powerpoint': powerpoint,
            #     'picture': picture,
            #     'video': video,
            #     'sound': sound,
            #     })
            # for i in A: print(i)
            return render(request, 'new.html',
                {'pg':True,
                'B': zip(C, A, k),
                'word': word,
                'excel': excel,
                'powerpoint': powerpoint,
                'picture': picture,
                'video': video,
                'sound': sound,
                }
            )
    elif request.method == 'POST' and request.POST.get('action') == 'change':
        changed = request.POST.get('file_name')[:100]
        root = request.POST.get('change_name')
        ext = request.POST.get('ext')
        if root is not None and changed is not None:
            file_name = root + '.' + ext
            for file in File.objects.filter(folder = Folder.objects.get(id = just_a_little_bit_course)):
                if file_name == file.name:
                    file.name = changed + '.' + ext
                    file.save()
                    break
        # if root is not None and root in 
        A = []
        C = []
        k = File.objects.filter(folder = Folder.objects.get(id = just_a_little_bit_course))
        for file in k:
            A.append(os.path.splitext(file.name)[1].lower().lstrip('.'))
            C.append(os.path.splitext(file.name)[0])
        return render(request, 'new.html',
            {'pg':True,
            'B': zip(C, A, k),
            'word': word,
            'excel': excel,
            'powerpoint': powerpoint,
            'picture': picture,
            'video': video,
            'sound': sound,
            }
        )
    else:
        folder_form = FolderForm()
        return render(request, 'new.html', {'folder_form': folder_form, 'pg':False})
def subhome(request):
    global just_a_little_bit_course
    if just_a_little_bit_course:
        k = Folder.objects.get(id = just_a_little_bit_course)
        k.state = True
        k.save()
        # fol = f_form.save()
        # # print(fol)
        # # print(file_2)
        # for idx, i in enumerate(file_2, File.objects.filter(folder=fol).count() + 1):
        #     f = File(name = f'{i}', folder=fol, file=i, index = idx)
        #     # print(i)
        #     # # open(f)
        #     # print(f)
        #     # f.open()
        #     f.save()
    return redirect('home')

def listhome(request, id):
    if request.user.is_authenticated:
        A = []
        C = []
        x = Folder.objects.get(id = id)
        k = File.objects.filter(folder = x)
        for file in k:
            A.append(os.path.splitext(file.name)[1].lower().lstrip('.'))
            C.append(os.path.splitext(file.name)[0])
        return render(request, 'list.html', {
            'fold': x,
            'B': zip(C, A, k),
            'word': word,
            'excel': excel,
            'powerpoint': powerpoint,
            'picture': picture,
            'video': video,
            'sound': sound,
            }
        )
    else: return redirect("home")