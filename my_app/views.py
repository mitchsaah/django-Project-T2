from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from .models import Article

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
    context_object_name = 'articles'