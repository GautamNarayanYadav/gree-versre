from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from g_vers.models import Photography, Contact
from g_vers.serializers import ContactSerializer


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['picture'] = Photography.objects.all()[:8]
        return context


class PhotographyView(TemplateView):
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        context = super(PhotographyView, self).get_context_data(**kwargs)
        context['photos'] = Photography.objects.all()
        # context['page_data'] = Photography.objects.latest('id')
        # context['auto_data'] = Auto.objects.all()[:4]
        # context['expert_data'] = Expert.objects.all()[:3]
        return context


def detail_page(request, id):
    obj = get_object_or_404(Photography, pk=id)
    return render(request, 'photo-detail.html', {'obj': obj})


def contact_view(request):
    model = Contact
    return render(request, "contact.html")


class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
