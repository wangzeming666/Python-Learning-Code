from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen as uopen
import pdb
REGEX = compile(b'#([\d,]+) in Books')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals'
    }
def getRanking(isbn):
    page = uopen('%s%s' %(AMZN, isbn))
    data = page.read()
    page.close()
    return REGEX.findall(data)[0].decode('utf-8')

def _showRanking(isbn):
    print('- %r ranked %s' %(ISBNs[isbn], getRanking(isbn)))

def _main():
    print('At', ctime(), 'on Amazon')
    for isbn in ISBNs:
        Thread(target=_showRanking, args=(isbn,)).start()

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()
