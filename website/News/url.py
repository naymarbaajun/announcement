from django.urls import path
from. import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login', views.login),
    path('form', views.form),
    path('news', views.news),
    path('academic', views.academic),
    path('event', views.event),
    path('loan', views.loan),
]
