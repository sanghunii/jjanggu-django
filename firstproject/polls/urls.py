from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>", views.detail),
    path("<int:question_id>/results", views.results),
    path("<int:question_id>/vote", views.vote),
    path("api_get", views.api_get, name="api-get"),
    path("drf_api", views.drf_api, name="drf_api"),
]