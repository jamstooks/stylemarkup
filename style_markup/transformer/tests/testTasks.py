from django.test import TestCase

from style_markup.transformer.tasks import load_gist

class TestTasks(TestCase):
    
    def setUp(self):
        pass
        
    def testGist(self):
        gist = load_gist("7819035", "rst")
        self.assertEqual('gistfile1.rst', gist[1])
        