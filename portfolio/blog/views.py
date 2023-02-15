from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView

from common.views import TitleMixin

from .models import BlogModel


class BlogView(TitleMixin, ListView):
    title = 'Blog'
    template_name = 'blog/all_blogs.html'
    model = BlogModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = self.model.objects.all().order_by('-date_creation')
        return context


def detail(request, blog_id):
    blog = get_object_or_404(BlogModel, pk=blog_id)
    return render(
        request,
        template_name='blog/detail.html',
        context={'blog': blog},
    )
