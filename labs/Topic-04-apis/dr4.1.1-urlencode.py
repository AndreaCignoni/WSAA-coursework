# Strings need to be encoded when they are used in URLs. URLs have a specific format, 
# and certain characters, such as spaces or special characters, may not be allowed in their raw form. 
# Encoding is the process of converting special characters into a format that can be safely used in a URL.

# The urllib library in Python provides modules to work with URLs:
# 1. urllib.parse: This module provides functions to manipulate URLs:
# - 'quote(string, safe=''): This function is used to URL-encode a string. It replaces special characters with their corresponding percent-encoded values. 
# - 'unquote(string): This function is used to decode a URL-encoded string back to its original form.
# 2. urllib.request: This module is used for opening and reading URLs. It provides functions for making HTTP requests, handling cookies, and more.

import urllib
from urllib.parse import quote
query = 'Hellö Wörld@python'
parsed = urllib.parse.quote(query)
print(parsed)
# Hell%C3%B6%20W%C3%B6rld%40python

params = {'q': 'Python URL encoding', 'as_sitesearch': 'www.urlencoder.io'}
parsedparams = urllib.parse.urlencode(params)
print(parsedparams)
# q=Python+URL+encoding&as_sitesearch=www.urlencoder.io