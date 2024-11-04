from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Article
from django import forms
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

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
    ordering = ['-created_at']

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

@login_required
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/edit_article.html', {'form': form, 'article': article})

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/delete_article.html'
    success_url = reverse_lazy('article_list')

    def get_queryset(self):
        # Limit deletion to the article owner
        return self.model.objects.filter(author=self.request.user)