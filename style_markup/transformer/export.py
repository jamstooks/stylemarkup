from django.template.loader import get_template
from django.template import Context

import cStringIO as StringIO
import ho.pisa as pisa

import sys

def render_to_pdf(template_src, context_dict):
    """
        Creates a pdf from a temlate and context
        Returns a StringIO.StringIO object
    """

    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(html, result)

    if not pdf.err:
        return result.getvalue()
    else:
        # msg = "PDF Generation Failed %s" % html
        # print >> sys.stderr, msg
        # logger.error(msg)
        return None