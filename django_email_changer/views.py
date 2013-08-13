# Copyright 2013 Tom Aratyn <tom@aratyn.name>
#
# This program is licensed under the MIT license (see LICENSE or http://opensource.org/licenses/MIT)
#

from threading import Thread

from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import FormView
from django.views.generic.base import RedirectView

from django_email_changer import settings
from django_email_changer.forms import UserEmailModificationForm
from django_email_changer.models import UserEmailModification


class CreateUserEmailModificationRequest(FormView):
    
    form_class = UserEmailModificationForm
    http_method_names = ["get", "post", ]
    success_url = settings.EMAIL_CHANGE_SUCCESS_URL
    template_name = "django_email_changer/change_email_form.html"

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            if not request.user.check_password(form.cleaned_data.get("password")):
                form.errors["password"] = [u'Wrong password.']
                return self.form_invalid(form)
            new_email = form.cleaned_data.get("new_email")
            uem = UserEmailModification.objects.create(user=request.user, new_email=new_email)
            email_body = render_to_string(settings.EMAIL_CHANGE_NOTIFICATION_EMAIL_TEMPLATE,
                                          {"email_modification": uem, })
            thread = Thread(target=send_mail,
                            args=[settings.EMAIL_CHANGE_NOTIFICATION_SUBJECT,
                                  email_body,
                                  settings.EMAIL_CHANGE_NOTIFICATION_FROM,
                                  (uem.new_email, )],
                            kwargs={"fail_silently": True})
            thread.setDaemon(True)
            thread.start()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ActivateUserEmailModification(RedirectView):

    http_method_names = ['get', ]
    permanent = False
    url = settings.EMAIL_CHANGE_ACTIVATION_SUCCESS_URL

    def get(self, request, code, *args, **kwargs):
        uem = get_object_or_404(UserEmailModification, security_code__exact=code, user__exact=request.user)
        if uem.activate():
            return super(ActivateUserEmailModification, self).get(request, *args, **kwargs)
        else:
            raise Http404()