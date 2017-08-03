from django.shortcuts import render
from django.views.generic import View, TemplateView,ListView,DetailView
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'

    # to create a context dictionary for injecting data into templates
    def get_context_data(self,**kwargs):
        # passing in self and keyword arguments
        context = super().get_context_data(**kwargs)
        context['injection'] = 'display this message on the index page'
        return context

class SchoolListView(ListView):
    model = models.School
    # template_name = 'basic_app/school_list.html' <- this is the default template name
    # this returns a context dictionary named school_list
    # lowercase model name underscore list, (snake_case)
    # we can change the name of this context dictionary like so
    # context_object_name = 'schools'

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'
    # detail view will just return school (lowercase model name)
