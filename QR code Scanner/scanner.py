import pyqrcode
import png
from pyqrcode import QRCode

link='https://www.wikipedia.org/'
url=pyqrcode.create(link)
url.png('wikipediaqrcode.png',scale=6)