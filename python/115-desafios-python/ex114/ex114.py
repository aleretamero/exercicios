import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site está off-line')
else:
    print('O site está online')
    print(site.read())
