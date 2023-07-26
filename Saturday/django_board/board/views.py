from django.shortcuts import render, redirect, HttpResponse
from .models import User, Question, Answer
from .forms import ArticleForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def test(request):
    return HttpResponse("<h1>AI12기 여러분 반갑습니다.")

def question_list(request):
    queststionlist = Question.objects.all()
    return render(request, 'question_list.html', {'qlist':queststionlist})

@csrf_exempt
def question_create(request): 
    if request.method == 'GET':
        form = ArticleForm()
        context={
            'form':form
        }
        return render(request,'question_create.html', context)
    elif request.method =='POST':
        form =ArticleForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('board')
