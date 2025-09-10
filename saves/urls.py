# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path

# Internal:
from saves import views

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

urlpatterns = [
    path("saves/", views.SaveList.as_view()),
    path("saves/<int:pk>/", views.SaveDetail.as_view()),
    path("my-saves/", views.UserSaveList.as_view()),
]
