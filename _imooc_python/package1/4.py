a = 1
while a<=5:
    print(a)
    a += 1
else:
    print('down')

b = ['a','b','c','d','e']
for y in range(0,6,2):
    for x in b:
        if x == 'c':
            continue
        print(x,end='')
        print(y)
