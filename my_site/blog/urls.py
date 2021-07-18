from django.urls import path
from . import views

urlpatterns =[
    path('', views.about_site,name='about_site'),
    path('post',views.post_list,name='post_list'),
    path('post/<slug:slug>',views.post_detail,name='post_detail'),
]
