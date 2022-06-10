from django.shortcuts import render
import random

# Create your views here.
def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'index.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    lenght = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        characters.extend(list('!"·$%&/()=<>*^¨+-_'))

    if request.GET.get('number'):
        characters.extend(list('1234567890'))
    for x in range(lenght):
        generated_password += random.choice(characters)

    context = {'password': generated_password}
    return render(request, 'password.html', context)