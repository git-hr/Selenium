import re

a = '6sd4fsd4fds4f8924sd9f4sd84f'

# r = re.findall('[a-zA-Z0-9]{1,6}?o' ,a)
# s = re.findall('你好$' ,a)

def convert(value):
    match = value.group()
    if int(match) >= 50:
        return '99'
    else:
        return '00'

t = re.sub('(\d\d)' ,convert ,a)
r = re.search('4' ,a)
print(r.span())
# print(r,s)
print(t)