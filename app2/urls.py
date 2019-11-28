from django.urls import path
from app2 import views
app_name="app2"
urlpatterns = [
    path("home/",views.home,name="home_app2"),
]