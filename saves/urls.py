from django.urls import path
from saves import views

urlpatterns = [
    path('saves/', views.SaveList.as_view())
    ]