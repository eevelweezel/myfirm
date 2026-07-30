from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from . import forms, models

class Home(TemplateView):
    template_name = "myfirm/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sections"] = models.Section.objects.filter(published=True)
        context["info"] = models.Info.objects.filter(active=True) # should only be ONE!
        context["form"] = forms.Contact()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        form = forms.Contact(request.POST)
        if form.is_valid():
            # Send an email & display "SUCCESS" message inline
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            contact_email = form.cleaned_data["contact_email"]

            body = (
                "Submitted through the contact form.\n"
                f"Contact email (unverified): {contact_email}\n"
                f"Message:\n{message}"
            )

            EmailMessage(
                subject=f"[contact form] {subject}",
                body=body,
                from_email=settings.TO_EMAIL,
                to=[settings.TO_EMAIL],
                reply_to=[contact_email],
            ).send()

            messages.success(request, "Thanks! We'll get back to you shortly!")
        return render(request, self.template_name, context)
