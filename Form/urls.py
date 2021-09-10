from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('jsonData', views.jsonData, name='json'),
    path('ses', views.ses, name='ses'),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('addEvent', views.addEvent, name='addEvent'),
    path('showEvent/<eid>/', views.showEvent, name='showEvent'),
]
