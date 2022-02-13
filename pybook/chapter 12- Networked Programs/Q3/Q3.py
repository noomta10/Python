import ssl
import urllib.request
import urllib.parse

from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

request = urllib.request.Request("https://www.tapuz.co.il/")
request.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                   " Chrome/97.0.4692.99 Safari/537.36")
html = urllib.request.urlopen(request, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

images = soup('img')
for image in images:
    file = open("image.PNG", "wb")
    src = image.get('src', None)
    if not src.startswith("http"):
        src = "https://www.tapuz.co.il" + src
    print('1', src)
    src_ending = src[8:]
    print("2", src_ending)
    src_ending = urllib.parse.quote(src_ending.encode('utf8'))
    print("3", src_ending)
    final_src = "https://" + src_ending
    request = urllib.request.Request(final_src)

    request.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                       " Chrome/97.0.4692.99 Safari/537.36")
    image = urllib.request.urlopen(request, context=ctx).read()
    file.write(image)
    file.close()
