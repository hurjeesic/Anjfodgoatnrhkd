from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Example
from .models import Dialect
from . import function
import random

problem_num = 20

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

    count = 0
    lst = set()
    while len(lst) < problem_num:
        lst.add(random.randrange(0, len(dialects)))

    lst = list(lst)

    problems = []
    for num in range(problem_num):
        answer_num = random.randrange(1, 5)
        word = dialects[lst[num]]
        lst[num] = { 'num': num + 1, 'problem': word.jeju, 'answer_num': answer_num }
        for i in range(1, 5):
            if i == answer_num: lst[num][str(i)] = word.standard
            lst[num][str(i)] = dialects[random.randrange(0, len(dialects))].standard

    return render(request, 'quiz/quiz.html', {'problems': lst})

# request 사용법
# https://victorydntmd.tistory.com/260
def result(request):
    score = 0
    for num in range(1, problem_num + 1):
        try:
            if request.POST['p.' + str(num)] == request.POST['a.' + str(num)]:
                score += 100 / problem_num
        except KeyError:
            pass

    return render(request, 'quiz/result.html', { 'score': str(score) })

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
