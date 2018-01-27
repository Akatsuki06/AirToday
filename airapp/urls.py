from django.urls import path
from airapp import views

urlpatterns=[
path('',views.IndexView.as_view(),name='index'),
path('register/',views.RegisterView.as_view(),name='register'),
]
