import re
import ssl
import urllib.error
import urllib.request
from urllib.parse import unquote


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://blogs.tapuz.co.il/wp-json/authorpost/v1/get_get_author_listing/?count=22"

request = urllib.request.Request(url)
request.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36")
html = urllib.request.urlopen(request).read()
title_matches = re.findall("\"title\":\"(.+?)\"", html.decode())
main_title = title_matches[0]
print(main_title.encode('latin1').decode('unicode_escape'))
# print(u'\\u05d2\\u05d0\\u05d5\\u05d5\\u05d4 \\u05d9\\u05e9\\u05e8\\u05d0\\u05dc\\u05d9\\u05ea:'.encode('latin1').decode('unicode_escape'))
