from django.shortcuts import render
from django.utils import timezone
from .models import Example

# Create your views here.
def index(request):
    examples = Example.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'quiz/index.html', {'examples': examples})

def quiz(request):
    return render(request, 'quiz/quiz.html', {})

def dictionary(request):
    return render(request, 'quiz/dictionary.html', {})

def help(request):
    return render(request, 'quiz/help.html', {})
