import requests
import markdown
from docutils.core import publish_parts
from django.utils.safestring import mark_safe

# @todo: start using celery

def load_gist(id, markup):
    """
        Pulls the content of a gist using the github api
    """
    r = requests.get("https://api.github.com/gists/%s" % id)
    json = r.json()
    
    for k, f in json["files"].items():
        # only grab the first file
        filename = f['filename']
        if markup == "rst":
            content = convert_rst(f["content"])
        elif markup == "md":
            content = "<div class='document'>%s</div>" % convert_md(f["content"])
    
    return json, filename, mark_safe(content)

def convert_rst(rst):
    """
        Uses docutils to convert rst to html
    """
    return publish_parts(rst,writer_name='html')['html_body']

def convert_md(md):
    """
        Uses markdown library to convert md to html
    """
    return markdown.markdown(md)