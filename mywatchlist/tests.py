from django.test import TestCase
from django.test import Client

# Test if the reponse of the HTML, XML, and JSON path equals to 200
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