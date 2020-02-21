from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("status/", views.ServerStatusView.as_view()),
]
