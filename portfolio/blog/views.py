from django.views.generic.list import ListView

from common.views import TitleMixin
from .models import BlogModel


class BlogView(TitleMixin, ListView):
    title = 'Blog'
    template_name = 'blog/all_blogs.html'
    model = BlogModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = self.model.objects.all()
        return context
