#-*- coding: utf-8 -*-

from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404

from blog.forms import NewContactForm
from .forms import ContactForm

# Create your views here.
from blog.models import Article, Contact


def view_article(request, id_article):
    """
    seeing that it displays an article according to its identifier(where id, here is a numbe
    it id it's the second function parameter ( the first one is always the user request
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


def read(request, article_id):
    """View a complete article"""
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/read.html', {'article': article})


def contact(request):
    # build the form, either with the data posted
    # either empty, if the user accessed, for the first time to the page
    form = ContactForm(request.POST or None)
    # you verify that the data sent is valid
    # this method return false if there is no data
    # in the form or that contains errors
    if form.is_valid():
        # here you can treat the form data
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        renvoi = form.cleaned_data['renvoi']

        # here you could send an email with the data
        # that you have recovred
        send = True

    # whatever happens, the form page is displayed
    return render(request, 'blog/contact.html', locals())


def new_contact(request):
    saving = False
    form = NewContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.name = form.cleaned_data["name"]
        contact.address = form.cleaned_data["address"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        saving = True

    return render(request, 'blog/new_contact.html', {
        'form': form,
        'saving': saving
    })


def show_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'blog/show_contacts.html', {'contacts': contacts})

