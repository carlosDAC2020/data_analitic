from django.urls import path 
from . import views

app_name = 'analitic'

urlpatterns = [
    path('', views.home, name="home" ),
    path('cargar_csv/', views.create_analiric_space, name='cargar_csv'),
]