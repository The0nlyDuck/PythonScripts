import mmap
from time import strftime

date = str.encode(strftime("%d %b %Y"))

f = open('C:\\Users\\nathan\\Desktop\\School Work\\Year 11\\IT-Programming\\Sudoku list.txt')
s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
if s.find(date) != -1:
    print('true')
elif s.find(date) == -1:
    print('false')

#https://stackoverflow.com/questions/4940032/how-to-search-for-a-string-in-text-files
#this is the site where the main part of this is from, it is the top answer

#https://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3
#this site was use to know how to change a string into bytes