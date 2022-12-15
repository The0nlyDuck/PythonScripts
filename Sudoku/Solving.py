import pprint as pp

Sadoku = [['3', '0', '0'],
 ['0', '9', '0'],
 ['0', '4', '0'],
 ['0', '0', '7'],
 ['5', '2', '0'],
 ['0', '0', '9'],
 ['2', '0', '0'],
 ['3', '8', '0'],
 ['5', '0', '6'],
 ['2', '1', '0'],
 ['8', '0', '0'],
 ['0', '0', '4'],
 ['0', '7', '0'],
 ['9', '0', '5'],
 ['0', '8', '0'],
 ['9', '0', '0'],
 ['0', '0', '7'],
 ['0', '5', '3'],
 ['7', '0', '9'],
 ['0', '3', '1'],
 ['0', '0', '6'],
 ['3', '0', '0'],
 ['0', '6', '2'],
 ['1', '0', '0'],
 ['0', '1', '0'],
 ['0', '4', '0'],
 ['0', '0', '5']]


#The Vertical lines in the Sadoku puzzle
row1 = [[Sadoku[0][0], Sadoku[1][0],Sadoku[2][0]], [Sadoku[9][0],Sadoku[10][0],Sadoku[11][0]],[Sadoku[18][0],Sadoku[19][0],Sadoku[20][0]]]
row2 = [[Sadoku[0][1], Sadoku[1][1],Sadoku[2][1]],[Sadoku[9][1],Sadoku[10][1],Sadoku[11][1]],[Sadoku[18][1],Sadoku[19][1],Sadoku[20][1]]]
row3 = [[Sadoku[0][2], Sadoku[1][2],Sadoku[2][2]],[Sadoku[9][2],Sadoku[10][2],Sadoku[11][2]],[Sadoku[18][2],Sadoku[19][2],Sadoku[20][2]]]

row4 = [[Sadoku[3][0], Sadoku[4][0],Sadoku[5][0]],[Sadoku[12][0],Sadoku[13][0],Sadoku[14][0]],[Sadoku[21][0],Sadoku[22][0],Sadoku[23][0]]]
row5 = [[Sadoku[3][1], Sadoku[4][1],Sadoku[5][1]],[Sadoku[12][1],Sadoku[13][1],Sadoku[14][1]],[Sadoku[21][0],Sadoku[22][0],Sadoku[23][0]]]
row6 = [[Sadoku[3][2], Sadoku[4][2],Sadoku[5][2]],[Sadoku[12][2],Sadoku[13][2],Sadoku[14][2]],[Sadoku[21][0],Sadoku[22][0],Sadoku[23][0]]]

row7 = [[Sadoku[6][0], Sadoku[7][0],Sadoku[8][0]],[Sadoku[15][0],Sadoku[16][0],Sadoku[17][0]],[Sadoku[24][0],Sadoku[25][0],Sadoku[26][0]]]
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



pp.pprint(alist)
print(" ")
pp.pprint(blist)
print(" ")
pp.pprint(clist)

for n in range(0,3):
    for m in range(0,3):
        if lines[m][m][n] == rows[n][n][m]:
            print("F")