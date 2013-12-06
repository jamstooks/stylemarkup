from django import forms
import re

class MarkupForm(forms.Form):
    source = forms.URLField()
    markup = forms.ChoiceField(choices=(('rst', "reStructuredText"), ('md', "Markdown")))
    
    def __init__(self, *args, **kwargs):
        super(MarkupForm, self).__init__(*args, **kwargs)
        
        self.fields['source'].widget.attrs = {'placeholder': "https://gist.github.com/user/#######"}
    
    def clean_source(self):
        """
            Make sure this matches the regex for gist 
            if so, return the gist id
        """
        source = self.cleaned_data['source']
        
        gist_pattern = "https://gist.github.com/([^/]+)/([^/]+)/?.*"
        m = re.match(gist_pattern, source)
        
        if not m:
            raise forms.ValidationError("Hmm... this should look like: https://gist.github.com/<user>/<id>")
            
        return m.group(2)
            