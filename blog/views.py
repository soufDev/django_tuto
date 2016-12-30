#-*- coding: utf-8 -*-

from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render


# Create your views here.


def home(request):
    """Html page example, not valid for the example to be concise"""
    text = """<h1>Welcome to my blog !!</h1>
                <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)


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

