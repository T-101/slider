from django.contrib.auth.views import LoginView as DjangoLoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import translation
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.translation import check_for_language
from django.views.generic import FormView, TemplateView, View
from slider.mixins import LoginRequiredMixin
from django.conf import settings

from slider.forms import PictureForm
from slider.models import Settings


class IndexView(FormView):
    template_name = "slider/index.html"
    form_class = PictureForm
    success_url = reverse_lazy("slider:index")

    def form_valid(self, form):
        if not Settings.load().uploads_enabled:
            return super().form_invalid(form)
        form.save()
        return super().form_valid(form)


class SliderView(TemplateView):
    template_name = "slider/slider.html"


class LoginView(DjangoLoginView):
    template_name = 'slider/login.html'
    next_page = reverse_lazy("slider:admin")


class AdminView(LoginRequiredMixin, TemplateView):
    template_name = "slider/admin.html"


class SetLanguageView(View):
    def get(self, request, *args, **kwargs):
        # Copied from django.views.i18n.set_language

        lang_code = kwargs.get("language")

        next_url = request.META.get('HTTP_REFERER')
        if not url_has_allowed_host_and_scheme(next_url, settings.ALLOWED_HOSTS, require_https=not settings.DEBUG):
            next_url = '/'
        response = HttpResponseRedirect(next_url)
        if lang_code and check_for_language(lang_code):
            translation.activate(lang_code.lower())
            max_age = 365 * 24 * 60 * 60  # One year
            response.set_cookie(key=settings.LANGUAGE_COOKIE_NAME, value=lang_code.lower(), max_age=max_age)
        return response
