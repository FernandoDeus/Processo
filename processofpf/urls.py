"""Criei os links das páginas e aplicações
"""
from django.contrib import admin
from django.urls import path
from sistema.views import home, form, create, view, edit, update, delete, sim

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('sim/', sim, name='sim'),
]
