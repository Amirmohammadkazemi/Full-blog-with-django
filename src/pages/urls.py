from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.Home, name='home'),
    path('blogs/<slug:slug>', views.Post, name='post'),
    path('category/<slug:slug>', views.Category, name='category'),
    path('blogs/', views.Blogs, name='blogpages'),
    path('projects', views.Projects, name='projects'),
    path('contact', views.Contact, name='contact'),
    path('support', views.Support, name='support'),
    path('aboutme', views.AboutMe, name='aboutme'),
]