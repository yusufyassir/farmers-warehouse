from django.urls import path
from . import views


urlpatterns = [
    path('', views.clpass),
    path('warehouse', views.WarehouseSet.as_view(
        {'get':'list',
         'post':'create'})
    ),
    path('warehouse/<str:batch>',views.SinglewarehouseSet.as_view()),
]
