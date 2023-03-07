from django.urls import path
from polls.views import list_view

app_name = "polls"
urlpatterns = [
    path("", list_view, name="list"),
]
