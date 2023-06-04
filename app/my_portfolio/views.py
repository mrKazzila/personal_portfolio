from django.views.generic.list import ListView

from common.views import TitleMixin
from .models import Project


class HomeView(TitleMixin, ListView):
    """Main page"""

    title = 'Portfolio'
    template_name = 'my_portfolio/portfolio.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.model.objects.all()
        return context
