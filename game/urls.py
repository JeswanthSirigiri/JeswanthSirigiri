from django.urls import path
from game import views

urlpatterns = [
    path('',views.home),
    path('read',views.score_card)
]