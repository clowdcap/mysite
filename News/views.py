from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from .models import DataRegistro, News, Newsletter
from .forms import RegisterForms
from .newsletter import RegisterNewsletter
from django.contrib import messages
from django.template import RequestContext
from datetime import datetime




def home(request):
    context = {
        "text": "jose.marinho56@gmail.com",
        "nomes": ["Jose", "Maria", "Joao", "Luana"],
        "form_news": RegisterNewsletter,
    }
    return render(request, "home.html", context)


def contato(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    context = {
        "horario": now,
        "horario2": current_time,
        "emailContent": "jose.marinho56@gmail.com",
        "telefoneContent": "(41) 99272-5388",
        "enderecoContent": "Rua tal, 250 - Sala 2 - Bairro X, Cidade-UF"
    }
    return render(request, "contato.html", context)


def news_details(request):

    obj = News.objects.all()
    context = {
        "object": obj,
    }
    return render(request, "news_details.html", context)


def news_anual(request, year):
    list = News.objects.filter(pub_date__year=year)
    context = {
        'year': year,
        'arquivo_list': list
    }
    return render(request, "news_anual.html", context)


def registro(request):
    context = {"form": RegisterForms}
    return render(request, "registro.html", context)

def add_user(request):
    form = RegisterForms(request.POST)

    if form.is_valid():
        registro = DataRegistro(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'],
                                email=form.cleaned_data['email'],
                                tel=form.cleaned_data['tel'])
        registro.save()
        
        messages.add_message(request, messages.SUCCESS, "Cadastro realizado com sucesso")
        
        return redirect('add') 
    
    
def add_newsletter(request):
    form_news= RegisterNewsletter(request.POST)

    if form_news.is_valid():
        registro_news = Newsletter(nome=form_news.cleaned_data['nome'],
                                emailnews=form_news.cleaned_data['emailnews'],)
                                
        registro_news.save()
        
        messages.add_message(request, messages.SUCCESS, "Cadastro realizado com sucesso")
        
        return redirect('home') 
    

def localizacao_projetos(request):
    context = {"form": RegisterForms}
    return render(request, "local.html", context)