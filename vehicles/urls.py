from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brands/post', views.brand_post, name='brand_post'),
    path('brands/put/<str:query_vehicle_brand>', views.brand_put, name='brand_put'),
    path('brands/get/<str:query_vehicle_brand>', views.brand_get, name='brand_get'),
    path('brands/delete/<str:query_vehicle_brand>', views.brand_delete, name='brand_delete'),
    
    path('types/post', views.type_post, name='type_post'),
    path('types/put/<str:query_vehicle_type>', views.type_out, name='type_put'),
    path('types/get/<str:query_vehicle_type>', views.type_get, name='type_get'),
    path('types/delete/<str:query_vehicle_type>', views.type_delete, name='type_delete'),
]