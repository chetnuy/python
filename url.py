'''
from urllib.parse import urlparse
# парсим адрес
url = urlparse('ftp://user:pass1@ya.ru')
print(url.hostname)
print(url.username)
'''

'''
# Парсим адресную строку из гугла
from urllib.parse import parse_qsl
s = 'https://www.google.ru/search?q=%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82&ie=utf-8&oe=utf-8&gws_rd=cr&ei=ZHFDWO-bFMHusAGlvqCYBQ#newwindow=1&q=%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82+%D0%BD%D0%B0+%D1%80%D0%B0%D0%B7%D0%BD%D1%8B%D1%85+%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0%D1%85'
arr = parse_qsl(s, encoding='utf-8')
print(arr)
'''

'''
#позволяет работать с относительными абсолютными путями
from urllib.parse import urljoin
s = urljoin('http://site.ru/f1/f2/f3/file.txt', 'foto.jpg')
print(s)
'''

