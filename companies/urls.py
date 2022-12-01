from django.urls import path

from . import views

urlpatterns = [
    path('post', views.post, name='company_post'),
    path('put/<str:cnpj>', views.put, name='company_put'),
    path('get/<str:cnpj>', views.get, name='company_get'),
    path('delete/<str:cnpj>', views.delete, name='company_delete'),
]