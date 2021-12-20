from django.shortcuts import render
from . import models as pagemodel
from config import models as configmodel

# Create your views here.
def Home(request):
    context = {
        'header': configmodel.Header.objects.all(),
        'articles': pagemodel.Article.objects.filter(ArticleStatus='Publish').order_by('-ArticleDate'),
        'sub': configmodel.Sub.objects.all(),
        'media': configmodel.Media.objects.all(),
    }
    return render(request, 'pages/index.html', context)

def Post(request, slug):
    context = {
    'article': pagemodel.Article.objects.get(ArticleSlug=slug),
    }
    return render(request, 'pages/post.html', context)

def AboutMe(request):
    context = {
        'aboutme': pagemodel.Aboutme.objects.all(),
    }
    return render(request, 'pages/aboutme.html', context)

def Projects(request):
    context = {
        'projects': pagemodel.Projects.objects.filter(ProjectStatus='Publish').order_by('-ProjectDate'),
    }
    return render(request, 'pages/projects.html', context)

def Contact(request):
    context = {
        'contact': pagemodel.Contact.objects.all(),
    }
    return render(request, 'pages/contact.html', context)

def Support(request):
    context = {
        'supports':
            #pagemodel.Support.objects.all(),
            pagemodel.Support.objects.filter(SupportStatus='Publish').order_by('SupportDate'),
    }
    return render(request, 'pages/support.html', context)

def Blogs(request):
    context = {
        'articles': pagemodel.Article.objects.filter(ArticleStatus='Publish').order_by('-ArticleDate'),
    }
    return render(request, 'pages/blogs.html', context)