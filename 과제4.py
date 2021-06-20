import turtle as t

with open('turtle.txt', 'r') as f:
    lines = f.readlines()
    value = list(map(int, lines))
    f.close()

t.shape('turtle')

for i in range(0, 7, 1):
    if (i % 2 == 0):
        t.forward(value[0])
    elif (i % 2 != 0):
        t.left(value[1])