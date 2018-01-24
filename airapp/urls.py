from django.urls import path
from airapp import views

urlpatterns=[
path('',views.funcView,name='funcview'),
path('index/',views.IndexView.as_view(),name='index')
]
