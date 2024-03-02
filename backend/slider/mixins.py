from django.contrib.auth.mixins import LoginRequiredMixin as DjangoLoginRequiredMixin
from django.urls import reverse


class LoginRequiredMixin(DjangoLoginRequiredMixin):
    redirect_field_name = 'redirect_to'

    def get_login_url(self):
        return reverse('slider:login')
