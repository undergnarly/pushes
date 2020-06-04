from django.shortcuts import render
from pushes.forms import PushesForm, PushesModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView
from pushes.models import Pushes


class PushesView(LoginRequiredMixin, FormView):
    template_name = 'pushes.html'
    form_class = PushesModelForm
    model = Pushes
    success_url = '/'
    

    def get_context_data(self, **kwargs):
        print(Pushes.objects.all())
        
        context = super(PushesView, self).get_context_data(**kwargs)
        context['all_pushes'] = Pushes.objects.all()
        return context
    
    def form_valid(self, form):
        title = form.cleaned_data['title']
        text = form.cleaned_data['text']
        published_date = form.cleaned_data['published_date']
        published = form.cleaned_data['published']
        new_push = Pushes(title=title, text=text, published_date=published_date, published=published)
        new_push.save()
        print(new_push.__dict__)

        return super(PushesView, self).form_valid(form)


class OptionsView(LoginRequiredMixin, TemplateView):
    template_name = 'options.html'

    def get_context_data(self, **kwargs):
        context = super(OptionsView, self).get_context_data(**kwargs)
        return context
        

# Create your views here.
