from django.contrib import admin
from django.urls import path, include
from my_app import views  # Importeer de views vanuit je app (ChatGPT)

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),  # Admin URL (ChatGPT)
    path('accounts/', include('django.contrib.auth.urls')),  # Ingebouwde login en logout routes (ChatGPT)
    path('register/', views.register, name='register'),  # Registratie route naar de register view (ChatGPT)
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('add/', views.add_article, name='add_article'), 

]

