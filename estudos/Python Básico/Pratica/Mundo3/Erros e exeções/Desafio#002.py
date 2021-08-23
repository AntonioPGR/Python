import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[31mNão consegui acessar o site do pudim')
else:
    print('\033[32mConsegui acessar o site do pudim!')
    print(site.read)