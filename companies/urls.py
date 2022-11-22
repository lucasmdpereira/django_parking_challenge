from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('put/<str:cnpj>', views.put, name='put'),
    path('get/<str:cnpj>', views.get, name='get'),
    path('delete/<str:cnpj>', views.delete, name='delete'),
]