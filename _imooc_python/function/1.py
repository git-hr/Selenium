from functools import reduce
import re

list_x = [1,2,3,4,5,6,7]
list_y = [7,6,5,4,3,2,1]
list_z = [(1,1),(-5,3),(4,5),(-3,-9),(5,0)]

step_x,step_y = zip(*list_z)
r1 = map(lambda x , y : x * y,list_x,list_y)
print(list(r1))

r_x = reduce(lambda x , y : x + y ,step_x,0)
r_y = reduce(lambda x , y : x + y ,step_y,0)
r2 = (r_x , r_y)
print(r2)

list_a = ['a','A','D','x','W']
r3 = filter(lambda x : re.search('[A-Z]',x),list_a)
print(list(r3))