from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Article
from django import forms
def home(request):
    recent_articles = Article.objects.order_by('-created_at')[:5]
    return render(request, 'base.html', {'recent_articles': recent_articles})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Saves user
            return redirect('login')  # After successful login
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'  #
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return HttpResponseRedirect(reverse('article_list'))
    else:
        form = ArticleForm()
    return render(request, 'articles/add_article.html', {'form': form})