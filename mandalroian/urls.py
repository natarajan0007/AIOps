from django.urls import path,include
from .import views

app_name = 'mandalroian'

urlpatterns = [
    path('chatwidget/',views.index,name='index'),
    path('netbot/',views.netbot,name='netbot'),
    path('mandalroian/',views.chatwidget,name='chatwidget')
]