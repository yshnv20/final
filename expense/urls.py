from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('add_expense/',views.add_expense,name='add_expense'),
    path('add_income/',views.add_income,name='add_income'),
    path('viewexpense/',views.viewexpense,name='viewexpense'),
    path('viewincome/',views.viewincome,name='viewincome'),

]