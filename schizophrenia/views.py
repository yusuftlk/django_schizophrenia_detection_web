from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import Resoults, Doctor
#from schizophrenia.models import Resoults, Doctor


def index(request):
    return render(request, 'resoults/index.html')

def ayrintilar(request, hasta_id):
    # try:
    #     resoult = Resoults.objects.get(pk = hasta_id)
    # except resoult.DoesNotExist:
    #     raise Http404('Hasta Kayıdı Mevcut Değil')
    resoult = get_object_or_404(Resoults, pk = hasta_id)
    context = {
        'resoult': resoult
    }
    return render(request, 'resoults/ayrintilar.html', context)

def list(request):
    resoults = Resoults.objects.all()
    context = {
        'resoults': resoults
    }
    return render(request, 'resoults/list.html', context)
#, Resoults.objects.all()

def add(request):
    return render(request, 'resoults/add.html')

def login(request):
    if request.methot == 'post':
        _username = request.post['username']
        _password = request.post['password']
        doctor = Doctor.objects.filter()
    return render(request, 'doctor/login.html')

def register(request):
    print("asd")
    if request.method == 'post':
        _name = request.post['name']
        _surname = request.post['surname']
        _username = request.post['username']
        _email = request.post['email']
        _password = request.post['password']
        _repassword = request.post['repassword']
        if _password == _repassword:
            if Doctor.objects.filter(username = _username).exists():
                print('bu kullanıcı adı daha önce alınmış')
                return redirect('register')
            else:
                if Doctor.objects.filter(email = _email).exists():
                    print('bu mail daha önce alınmış')
                    return redirect('register')
                else:
                    doctor = Doctor(name=_name, surname=_surname, username=_username, email = _email, password = _password )
                    doctor.save()
                    return redirect('login')
        else:
            print('parola eşleşmiyor')
            return redirect('register')

    return render(request, 'doctor/register.html')



