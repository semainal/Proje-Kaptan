from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='hakkımızda'),
    path('anilar',views.anilar, name='anılar'),
    path('gokyuzu',views.gokyuzu, name='gökyüzü')
    
]