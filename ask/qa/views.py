from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect 
from django.views.decorators.http import require_GET, require_POST
from django. core. paginator import Paginator, EmptyPage
from django.contrib import auth

from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm

def ask(request, *args, **kwargs):
    if request.method == "POST":
        form = AskForm(request.POST)
        if request.user.is_authenticated():
            form._user = request.user
        if form.is_valid():
            q = form.save()
            return HttpResponseRedirect('/question/' + str(q.pk) + '/')
    else:
        form = AskForm()
    return render(request, 'ask.html',{ 'form': form })     

@require_POST
def answer(request, *args, **kwargs):
    form = AnswerForm(request.POST)
    if request.user.is_authenticated():
            form._user = request.user
    if form.is_valid():
        a = form.save()
        return HttpResponseRedirect('/question/' + str(a.question.pk) + '/')
    else:
        return HttpResponseRedirect('/question/' + str(a.question.pk) + '/?err=1')    

@require_GET
def new_questions(request, *args, **kwargs):
    try:    
	questions = Question.objects.order_by('-added_at')
    except Question.DoesNotExist:
	raise Http404   		
    page = request.GET.get('page', 1)    
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request,'questions.html',{
	'questions': page.object_list,
	'paginator': paginator, 'page': page,
	})

@require_GET
def popular_questions(request, *args, **kwargs):
    try:    
	populars = Question.objects.order_by('-rating')
    except Question.DoesNotExist:
	raise Http404   		
    page = request.GET.get('page', 1)    
    paginator = Paginator(populars, 10)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request,'questions.html',{
	'questions': page.object_list,
	'paginator': paginator, 'page': page,
	})

def one_question(request, *args, **kwargs):
    if request.method is 'POST':
        return answer(request)
    id = kwargs['id']
    question = get_object_or_404(Question, id=id)		
    answers = Answer.objects.filter(question=question)
    return render(request,'question.html',{
	'question': question,
	'answers': answers,
	})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', { 'form': form })            

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.load()
            auth.login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', { 'form': form })            

def test(request, *args, **kwargs):
    return HttpResponse('OK')
