from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.views.generic import TemplateView


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
