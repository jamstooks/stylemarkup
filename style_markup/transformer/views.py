from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

from export import render_to_pdf
from tasks import load_gist

class TransformGist(TemplateView):
    """
        Loads the template that starts the async tasks that pulls the gist and
        converts it to html
    """
    template_name = "transformer/transform.html"
    
    def get_context_data(self, **kwargs):
        _c = super(TransformGist, self).get_context_data(**kwargs)
        _c['json'], _c['filename'], _c['styled_markup'] = load_gist(kwargs['id'], kwargs['markup'])
        return _c
        
class GistPDF(TransformGist):
    """
        Just changes the response from standard HTML to PDF
    """
    mimetype = 'application/pdf'
    extension = "pdf"
    template_name = "transformer/pdf.html"
    
    def render_to_response(self, context, **response_kwargs):
        """ Renders the excel file as a response """

        response = HttpResponse(mimetype=self.mimetype)
        response['Content-Disposition'] = ('attachment; filename=%s.%s' %
                                           (context['filename'],
                                           self.extension))
        f = render_to_pdf(self.template_name, context)
        response.write(f)
        return response