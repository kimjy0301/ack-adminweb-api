from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("status/", views.ServerStatusView.as_view()),
    path("stats/emrifyear/", views.EmrifYearView.as_view()),
    path("stats/emrifweek/", views.EmrifWeekView.as_view()),
    path("stats/emrifdept/", views.EmrifDeptView.as_view()),
    path("stats/atypestatus/", views.AtypeStatusView.as_view()),
]
