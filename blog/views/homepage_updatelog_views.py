from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
from blog.models import HomePageUpdateModel


class HomeIndexView(generic.ListView):
    template_name = 'pages/main_home.html'
    model = HomePageUpdateModel
    paginate_by = 10

    def get_queryset(self):
        queryset = HomePageUpdateModel.objects.order_by('-updated_at')
        return queryset