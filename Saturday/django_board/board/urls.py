from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.test),
    path('question_list/', views.question_list, name='board'),
    path('question_create/', views.question_create),
]