Sadoku = [[0,0,0], [0, 0, 0], [0, 0, 0],
[0,0,0], [0, 0, 0], [0, 0, 0],
[0,0,0], [0, 0, 0], [0, 0, 0],
[0,0,0], [0, 0, 0], [0, 0, 0],
[0,0,0], [0, 0, 0], [0, 0, 0],
[0,0,0], [0, 0, 0], [0, 0, 0],
[0,0,0], [0, 0, 0], [0, 0, 0],
[0,0,0], [0, 0, 0], [0, 0, 0],
[0,0,0], [0, 0, 0], [0, 0, 0]]

a = ['0', '8', '5', '6', '0', '0', '0', '0', '4', '0', '0', '9', '1', '5', '0', '0', '2', '0', '1', '0', '0', '0', '0', '2', '0', '8', '7', '3', '7', '6', '5', '8', '0', '0', '0', '0', '0', '2', '0', '0', '0', '0', '0', '9', '0', '0', '0', '0', '0', '4', '6', '7', '3', '8', '6', '1', '0', '9', '0', '0', '0', '0', '3', '0', '3', '0', '0', '7', '1', '4', '0', '0', '8', '0', '0', '0', '0', '4', '2', '5', '0']

index = 0
for k in range(0, 3):
    for i in range(0,3):
        for j in range(0,3):
            left = i * 3 + j * 9 + 27 * k
            right = left + 3
            Sadoku[index] = a[left:right]
            index = index + 1

print(Sadoku)