from django.contrib import admin
from django.urls import path, include
from my_app import views  # Importeer de views vanuit je app (ChatGPT)

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL (ChatGPT)
    path('accounts/', include('django.contrib.auth.urls')),  # Ingebouwde login en logout routes (ChatGPT)
    path('register/', views.register, name='register'),  # Registratie route naar de register view (ChatGPT)
]

