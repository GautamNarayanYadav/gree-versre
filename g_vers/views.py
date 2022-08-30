from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from g_vers.models import Photography


def index(request):
    return render(request, "index.html")


class PhotographyView(TemplateView):
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        context = super(PhotographyView, self).get_context_data(**kwargs)
        context['photos'] = Photography.objects.all()
        # context['page_data'] = Photography.objects.latest('id')
        # context['auto_data'] = Auto.objects.all()[:4]
        # context['expert_data'] = Expert.objects.all()[:3]
        return context
