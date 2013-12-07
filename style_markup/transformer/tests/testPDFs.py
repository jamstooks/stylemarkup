from django.test import TestCase
from django.conf import settings
from django.utils.safestring import mark_safe

from style_markup.transformer.export import render_to_pdf
from style_markup.transformer.tasks import convert_rst

class TestPDF(TestCase):
    
    def setUp(self):
        pass
        
    def testConversion(self):
        template_name = "transformer/pdf.html"
        _c = {}
        _c["project_path"] = settings.BASE_DIR
        
        rst = open("%s/transformer/tests/test.rst" % settings.BASE_DIR,'r')
        _c['styled_markup'] = mark_safe(convert_rst(rst.read()))
        rst.close()

        pdf = open("%s/transformer/tests/test.pdf" % settings.BASE_DIR, 'w')
        pdf.write(render_to_pdf(template_name, _c))
        pdf.close()
