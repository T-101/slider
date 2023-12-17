from django.urls import path

from slider.views import IndexView, SliderView

app_name = "slider"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("slider/", SliderView.as_view(), name="slider"),
]
