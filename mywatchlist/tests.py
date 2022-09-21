from django.test import TestCase
from django.test import Client

# Create your tests here.
client = Client()
response_html = client.get('/mywatchlist/html')
response_xml = client.get('/mywatchlist/xml')
response_json = client.get('/mywatchlist/json')

response_html.status_code
response_xml.status_code
response_json.status_code
