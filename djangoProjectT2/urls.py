from django.contrib import admin
from django.urls import path, include
from my_app import views  # Importeer de views vanuit je app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('accounts/', include('django.contrib.auth.urls')),  # Ingebouwde login en logout routes
    path('register/', views.register, name='register'),  # Registratie route naar de register view
]

