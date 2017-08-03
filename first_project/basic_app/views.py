from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View, TemplateView,
                                ListView,DetailView,
                                CreateView,UpdateView,
                                DeleteView)

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
    # context_object_name by default will just return school (lowercase model name)
    # context_object_name = 'school_detail' (we can of course, manually define our context_object_name)
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ("name","principal")
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
