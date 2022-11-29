from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('brands/post', views.brand_post, name='brand_post'),
    path('brands/put/<str:query_vehicle_brand>', views.brand_put, name='brand_put'),
    path('brands/get/<str:query_vehicle_brand>', views.brand_get, name='brand_get'),
    path('brands/delete/<str:query_vehicle_brand>', views.brand_delete, name='brand_delete'),
    
    path('types/post', views.type_post, name='type_post'),
    path('types/put/<str:query_vehicle_type>', views.type_put, name='type_put'),
    path('types/get/<str:query_vehicle_type>', views.type_get, name='type_get'),
    path('types/delete/<str:query_vehicle_type>', views.type_delete, name='type_delete'),
    
    path('models/post', views.model_post, name='model_post'),
    path('models/put/<str:query_vehicle_model>', views.model_put, name='model_put'),
    path('models/get/<str:query_vehicle_model>', views.model_get, name='model_get'),
    path('models/delete/<str:query_vehicle_model>', views.model_delete, name='model_delete'),
    
    path('post', views.vehicle_post, name='vehicle_post'),
    path('put/<str:query_vehicle>', views.vehicle_put, name='vehicle_put'),
    path('get/<str:query_vehicle>', views.vehicle_get, name='vehicle_get'),
    path('delete/<str:query_vehicle>', views.vehicle_delete, name='vehicle_delete'),
]