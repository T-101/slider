from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from slider.forms import PictureForm


class IndexView(FormView):
    template_name = "slider/index.html"
    form_class = PictureForm
    success_url = reverse_lazy("slider:index")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SliderView(TemplateView):
    template_name = "slider/slider.html"
