from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction', views.index, name='new_interaction'),
    path('social', views.social, name='social'),
    path('competitions', views.competitions, name='competitions'),
     path('library', views.library, name='library'),
     path('personal', views.personal, name='personal')
]
