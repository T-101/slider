from django.urls import path

from slider.views import IndexView, SliderView, LoginView, AdminView

app_name = "slider"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("slider/", SliderView.as_view(), name="slider"),
    path("login/", LoginView.as_view(), name="login"),
    path("admin/", AdminView.as_view(), name="admin"),
]
