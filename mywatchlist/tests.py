from django.test import TestCase
from django.test import Client

# Create your tests here.
class HTMLTestCase(TestCase):
    def test_html_response(self):
        client = Client()
        response_html = client.get('/mywatchlist/html')
        self.assertEqual(response_html.status_code, 200)

class XMLTestCase(TestCase):
    def test_json_response(self):
        client = Client()
        response_xml = client.get('/mywatchlist/xml')
        self.assertEqual(response_xml.status_code, 200)

class JSONTestCase(TestCase):
    def test_json_response(self):
        client = Client()
        response_json = client.get('/mywatchlist/json')
        self.assertEqual(response_json.status_code, 200)