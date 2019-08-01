from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Example
from .models import Dialect
from . import function

# Create your views here.
def index(request):
    return render(request, 'quiz/index.html', {})

def quiz(request):
    # if request.method == "POST":
    #     Example.objects.all().delete()
    #     lst = function.proverb_parsing()
    #     me = User.objects.get(username='anjfodgoatnrhkd')
    #     for sentence in lst:
    #         Example(author=me, sentence=sentence).save()
    #
    #     return redirect('index')

    # examples = Example.objects.all().order_by('sentence')
    dialects = Dialect.objects.all()

    return render(request, 'quiz/quiz.html', {'dialects': dialects})

def dictionary(request):
    # if request.method == "POST":
    #     Dialect.objects.all().delete()
    #     lst = function.dialect_parsing()
    #     for lang in lst:
    #         Dialect(standard=lang['standard'], jeju=lang['jeju']).save()
    #
    #     return redirect('index')

    datas = Dialect.objects.all() # .order_by('standard')
    temps = []
    dialects = []
    index = 1
    for data in datas:
        temps.append({'standard': data.standard, 'jeju': data.jeju})
        if index % 15 == 0:
            dialects.append(temps)
            temps = []
        index += 1

    return render(request, 'quiz/dictionary.html', {'dialects': dialects})

def help(request):
    return render(request, 'quiz/help.html', {})
