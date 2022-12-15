import sys, urllib.request, mmap, os
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import bs4 as bs
from time import strftime
import time

filechecker = os.path.isfile('C:\\Users\\Public\\Documents\\Sudoku list.txt')
if filechecker == False:
    file1 = 'Sudoku list.txt'
    path = 'C:\\Users\\Public\\Documents\\'
    connect = os.path.join(path, file1)
    check = open(connect, 'w')
    check.write("List: \n")
    check.close()

### Getting the daily puzzle ###
date = str.encode(strftime("%d %b %Y"))
f = open('C:\\Users\\Public\\Documents\\Sudoku list.txt')
s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)


#https://www.youtube.com/watch?v=FSH77vnOGqU
class Client(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()

sudokulist = open('C:\\Users\\Public\\Documents\\Sudoku list.txt', 'r')
fix = list(sudokulist)
todayzpuz = []


if s.find(date) == -1:
    unsolved = []

    url = 'http://sudoku.com.au/'
    client_response = Client(url)
    source = client_response.mainFrame().toHtml()
    soup = bs.BeautifulSoup(source, 'lxml')
    js_test = soup.find('table', class_= "sudokutable")
    for i in range(0,81):
        js2 = js_test.find_next('td')
        findB = js2.find('b')
        if findB == None:
            unsolved.append(str(0))
        else:
            unsolved.append(str(findB)[3:-4])
        js_test = js2

    write = open('C:\\Users\\Public\\Documents\\Sudoku list.txt', 'a')
    jk = "[" + strftime("%d %b %Y") + ", " + str(unsolved) + "]"
    write.writelines(jk + '\n')
    todayzpuz = unsolved

elif s.find(date) != -1:
    finalfix = fix[len(fix)- 1]
    todayzpuz = finalfix[14:-2]


#Cleaning the list to be usable
ff = list(todayzpuz)
for d in range(0,len(ff)):
     if '[' in ff:
        ff.remove('[')
     elif ',' in ff:
         ff.remove(',')
     elif ' ' in ff:
         ff.remove(' ')
     elif "'" in ff:
         ff.remove("'")
     elif ']' in ff:
         ff.remove(']')


#https://www.youtube.com/watch?v=FSH77vnOGqU
###--------------------------------------------------------------------------###



### Filling the Puzzle with the data from the website or .txt file ###

#The Sadoku puzzle empty, Box = [Top], [Middle], [Bottom], >next box<
Sadoku = [[0,0,0], [0, 0, 0], [0, 0, 0],
          [0,0,0], [0, 0, 0], [0, 0, 0],
          [0,0,0], [0, 0, 0], [0, 0, 0],

          [0,0,0], [0, 0, 0], [0, 0, 0],
          [0,0,0], [0, 0, 0], [0, 0, 0],
          [0,0,0], [0, 0, 0], [0, 0, 0],

          [0,0,0], [0, 0, 0], [0, 0, 0],
          [0,0,0], [0, 0, 0], [0, 0, 0],
          [0,0,0], [0, 0, 0], [0, 0, 0]]


index = 0
for k in range(0, 3):
    for i in range(0,3):
        for j in range(0,3):
            left = i * 3 + j * 9 + 27 * k
            right = left + 3
            Sadoku[index] = ff[left:right]
            index = index + 1

###--------------------------------------------------------------------------###



### Solving the Sudoku puzzle ###
#The Vertical lines in the Sadoku puzzle
row1 = [
        [Sadoku[0][0], Sadoku[1][0], Sadoku[2][0]],
        [Sadoku[9][0], Sadoku[10][0], Sadoku[11][0]],
        [Sadoku[18][0], Sadoku[19][0], Sadoku[20][0]]
       ]

row2 = [
        [Sadoku[0][1], Sadoku[1][1], Sadoku[2][1]],
        [Sadoku[9][1], Sadoku[10][1], Sadoku[11][1]],
        [Sadoku[18][1], Sadoku[19][1], Sadoku[20][1]]
       ]

row3 = [
        [Sadoku[0][2], Sadoku[1][2], Sadoku[2][2]],
        [Sadoku[9][2], Sadoku[10][2], Sadoku[11][2]],
        [Sadoku[18][2], Sadoku[19][2], Sadoku[20][2]]
       ]

row4 = [
        [Sadoku[3][0], Sadoku[4][0], Sadoku[5][0]],
        [Sadoku[12][0], Sadoku[13][0], Sadoku[14][0]],
        [Sadoku[21][0], Sadoku[22][0], Sadoku[23][0]]
       ]

row5 = [
        [Sadoku[3][1], Sadoku[4][1], Sadoku[5][1]],
        [Sadoku[12][1], Sadoku[13][1], Sadoku[14][1]],
        [Sadoku[21][0], Sadoku[22][0], Sadoku[23][0]]
       ]

row6 = [
        [Sadoku[3][2], Sadoku[4][2], Sadoku[5][2]],
        [Sadoku[12][2], Sadoku[13][2], Sadoku[14][2]],
        [Sadoku[21][0], Sadoku[22][0], Sadoku[23][0]]
       ]

row7 = [
        [Sadoku[6][0], Sadoku[7][0], Sadoku[8][0]],
        [Sadoku[15][0], Sadoku[16][0], Sadoku[17][0]],
        [Sadoku[24][0], Sadoku[25][0], Sadoku[26][0]]
        ]
row8 = [[Sadoku[6][0], Sadoku[7][0],Sadoku[8][0]],[Sadoku[15][0],Sadoku[16][0],Sadoku[17][0]],[Sadoku[24][1],Sadoku[25][1],Sadoku[26][1]]]
row9 = [[Sadoku[6][0], Sadoku[7][0],Sadoku[8][0]],[Sadoku[15][0],Sadoku[16][0],Sadoku[17][0]],[Sadoku[24][2],Sadoku[25][2],Sadoku[26][2]]]

#The Horiziotal lines in the Sadoku puzzle
line1 = [Sadoku[0][:3], Sadoku[3][:3], Sadoku[6][:3]]
line2 = [Sadoku[1][:3], Sadoku[4][:3], Sadoku[7][:3]]
line3 = [Sadoku[2][:3], Sadoku[5][:3], Sadoku[8][:3]]

line4 = [Sadoku[9][:3], Sadoku[12][:3], Sadoku[15][:3]]
line5 = [Sadoku[10][:3], Sadoku[13][:3], Sadoku[16][:3]]
line6 = [Sadoku[11][:3], Sadoku[14][:3], Sadoku[17][:3]]

line7 = [Sadoku[18][:3], Sadoku[21][:3], Sadoku[24][:3]]
line8 = [Sadoku[19][:3], Sadoku[22][:3], Sadoku[25][:3]]
line9 = [Sadoku[20][:3], Sadoku[23][:3], Sadoku[26][:3]]

#The Boxes in the Sadoku puzzle
box1 = [Sadoku[0][:3], Sadoku[1][:3], Sadoku[2][:3]]
box2 = [Sadoku[3][:3], Sadoku[4][:3], Sadoku[5][:3]]
box3 = [Sadoku[6][:3], Sadoku[7][:3], Sadoku[8][:3]]

box4 = [Sadoku[9][:3], Sadoku[10][:3], Sadoku[11][:3]]
box5 = [Sadoku[12][:3], Sadoku[13][:3], Sadoku[14][:3]]
box6 = [Sadoku[15][:3], Sadoku[16][:3], Sadoku[17][:3]]

box7 = [Sadoku[18][:3], Sadoku[19][:3], Sadoku[20][:3]]
box8 = [Sadoku[21][:3], Sadoku[22][:3], Sadoku[23][:3]]
box9 = [Sadoku[24][:3], Sadoku[25][:3], Sadoku[26][:3]]

lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9]
rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]
a = []
b = []
c = []


for m in range(0, 9):
    numberz = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for j in range(0, 3):
        for k in range(0, 3):
            if int(lines[m][j][k]) > 0:
                if int(lines[m][j][k]) in numberz:
                    numberz.remove(int(lines[m][j][k]))
            else:
                lines[m][j][k] = numberz
                alist = m, j, k
                a.append(alist)

for m in range(0, 9):
    numberz = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for j in range(0, 3):
        for k in range(0, 3):
            if int(rows[m][j][k]) > 0:
                if int(rows[m][j][k]) in numberz:
                    numberz.remove(int(rows[m][j][k]))
            else:
                rows[m][j][k] = numberz
                blist = m, j, k
                b.append(blist)

for m in range(0, 9):
    numberz = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for j in range(0, 3):
        for k in range(0, 3):
            if int(boxes[m][j][k]) > 0:
                if int(boxes[m][j][k]) in numberz:
                    numberz.remove(int(boxes[m][j][k]))
            else:
                boxes[m][j][k] = numberz
                clist = m, j, k
                c.append(clist)

###--------------------------------------------------------------------------###


### Putting the Sudoku Puzzle in a .txt to be visable
#A printed version of the Sudoku puzzle
location = 'C:\\Users\\Public\\Documents\\puzzle.txt'
puzzle = open(location, 'w')
puzzle.write(strftime("%d %b %Y") + "\n")
puzzle.write(str(line1[0]) + " " + "|" + " " + str(line1[1]) + " " + "|" + " " + str(line1[2]) + "\n")
puzzle.write(str(line2[0]) + " " + "|" + " " + str(line2[1]) + " " + "|" + " " + str(line2[2]) + "\n")
puzzle.write(str(line3[0]) + " " + "|" + " " + str(line3[1]) + " " + "|" + " " + str(line3[2]) + "\n")
puzzle.write("-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-"+ " " + "-"+ " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " +  "- \n")

puzzle.write(str(line4[0]) + " " + "|" + " " + str(line4[1]) + " " + "|" + " " + str(line4[2]) + "\n")
puzzle.write(str(line5[0]) + " " + "|" + " " + str(line5[1]) + " " + "|" + " " + str(line5[2]) + "\n")
puzzle.write(str(line6[0]) + " " + "|" + " " + str(line6[1]) + " " + "|" + " " + str(line6[2]) + "\n")
puzzle.write("-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-"+ " " + "-"+ " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " + "-" + " " +  "- \n")

puzzle.write(str(line7[0]) + " " + "|" + " " + str(line7[1]) + " " + "|" + " " + str(line7[2]) + "\n")
puzzle.write(str(line8[0]) + " " + "|" + " " + str(line8[1]) + " " + "|" + " " + str(line8[2]) + "\n")
puzzle.write(str(line9[0]) + " " + "|" + " " + str(line9[1]) + " " + "|" + " " + str(line9[2]) + "\n")

print('To find the sudoku puzzle go to: ' + location)

time.sleep(10)
