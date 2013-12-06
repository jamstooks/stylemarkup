from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from forms import MarkupForm

class Home(FormView):
    form_class = MarkupForm
    template_name = "home.html"
    
    def form_valid(self, form):
        url = reverse("gist", args=(form.cleaned_data['markup'], form.cleaned_data['source']))
        return HttpResponseRedirect(url)
