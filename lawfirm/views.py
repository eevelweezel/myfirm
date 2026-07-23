from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.views.generic import TemplateView

from . import forms

class Home(TemplateView):
    template_view = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sections"] = Sections.objects.filter(published=True)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_view(*args, **kwargs)
        content = self.template_view.render(context)
        return HttpResponse(content, status_code=200)

    def post(self, request, *args, **kwargs):
        context = self.get_context_view(*args, **kwargs)
        content = self.template_view.render(context)
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
                from_email="contact-form@example.com",
                to=["info@example.com"],
                reply_to=[contact_email],
            ).send()

            messages.success(request, "Thanks! We'll get back to you shortly!")
        return HttpResponse(content, status_code=200)
