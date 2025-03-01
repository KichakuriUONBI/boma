from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_income/', views.add_income, name='add_income'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('add_cattle/', views.add_cattle, name='add_cattle'),
    path('add_cattle_event/', views.add_cattle_event, name='add_cattle_event'),
]