import ssl
import urllib.error
import urllib.request

from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.walla.co.il/"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

h2_titles = soup('h2')
main_title = h2_titles[0]
print(main_title.contents[0])
