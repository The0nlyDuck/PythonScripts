import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import bs4 as bs
import urllib.request

class Client(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()


a = []

url = 'http://sudoku.com.au/'
client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup = bs.BeautifulSoup(source, 'lxml')
js_test = soup.find('table', class_= "sudokutable")
for i in range(0,81):
    js2 = js_test.find_next('td')
    findB = js2.find('b')
    if(findB == "None"):
        a.append(0)
    else:
        a.append(findB)
    js_test = js2

print(a)

#https://www.youtube.com/watch?v=FSH77vnOGqU