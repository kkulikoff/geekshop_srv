
import ordersapp.views as ordersapp
from django.urls import re_path, path

app_name="ordersapp"

urlpatterns = [
    path('', ordersapp.OrderList.as_view(), name='list'),
    path('create/', ordersapp.OrderCreate.as_view(), name='create'),
    path('update/<pk>/', ordersapp.OrderUpdate.as_view(), name='update'),
    path('delete/<pk>/', ordersapp.OrderDelete.as_view(), name='delete'),
    path('read/<pk>/', ordersapp.OrderRead.as_view(), name='read'),
    path('forming/complete/<pk>', ordersapp.forming_complete, name='forming_complete'),
    path('payment/result', ordersapp.payment_result, name='payment_result'),
    path('product/<int:pk>/price/', ordersapp.get_product_price)
]
