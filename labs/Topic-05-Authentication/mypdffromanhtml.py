# This is a test where I create my first pdf from an html page
# To do this I use an API generated from html2pdf.app
# Author: Andrea Cignoni

import requests
import urllib.parse
from config import apikeys as cfg

targetUrl = "https://en.wikipedia.org"

apiKey = cfg["htmltopdf"]

apiurl = 'https://api.html2pdf.app/v1/generate'

# Authentication is done by passing apiKey parameter to the request
params = {'url':targetUrl, 'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)
# An esample may be: "https://api.html2pdf.app/v1/generate?html=https://example.com&apiKey={your-api-key}"
requestUrl = apiurl +"?" + parsedparams

response = requests.get(requestUrl)
print (response.status_code)

result =response.content
with open("document2.pdf", "wb") as handler:
    handler.write(result)