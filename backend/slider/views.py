from django.contrib.auth.views import LoginView as DjangoLoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from slider.mixins import LoginRequiredMixin

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


class LoginView(DjangoLoginView):
    template_name = 'slider/login.html'
    next_page = reverse_lazy("slider:admin")


class AdminView(LoginRequiredMixin, TemplateView):
    template_name = "slider/admin.html"
