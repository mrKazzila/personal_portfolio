from django.shortcuts import render
from django.views.generic.base import TemplateView
from common.views import TitleMixin


class BlogView(TitleMixin, TemplateView):
    title = 'Portfolio'
    template_name = 'blog/all_blogs.html'

