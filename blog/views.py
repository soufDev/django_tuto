#-*- coding: utf-8 -*-

from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404

# Create your views here.
from blog.models import Article


def view_article(request, id_article):
    """
    seeing that it displays an article according to its identifier(where id, here is a numbe
    it id it's the second function parametre ( the first one is always the user request
    """
    if int(id_article) > 100:
        raise Http404
    return redirect('redirect_article')


def view_redirection(request):
    return HttpResponse("You were be redirected.")


def articles_list(request, month, year):
    """
    :param request:
    :param year:
    :param month:
    :return:
    """
    return HttpResponse("You Asked foc the Article of {0}-{1}".format(month, year))


def actual_date(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, number1, number2):
    total = int(number1) + int(number2)
    return render(request, 'blog/addition.html', locals())


def home(request):
    """View all article from our blog"""
    articles = Article.objects.all()
    return render(request, 'blog/home.html', {'last_articles': articles})


def read(request, id):
    """View a complete article"""
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/read.html', {'article': article})
