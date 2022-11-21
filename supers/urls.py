from django.urls import path
from . import views

urlpatterns = [
    path('', views.supers_list),
    path('<int:pk>/', views.supers_detail),
    path('custom/', views.hero_villain_lists)
]