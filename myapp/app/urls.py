from django.urls import path
from app import views

app_name = "app"
urlpatterns = [
    path("app/",views.test, name="test")
]