from django.urls import path, re_path

from orders import views

urlpatterns = [
    re_path(r'^orders/$', views.OrderList.as_view(), name='list'),
    re_path(r'^orders/create/$', views.OrderCreate.as_view(), name='Create'),
    re_path(r'^orders/update/(?P<pk>[0-9]+)/$', views.OrderUpdate.as_view()),
    re_path(r'^orders/delete/(?P<pk>[0-9]+)/$', views.OrderDelete.as_view(), name='Delete'),

]
