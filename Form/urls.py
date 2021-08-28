from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('jsonData', views.jsonData, name='json'),
    path('ses', views.ses, name='ses'),
]
