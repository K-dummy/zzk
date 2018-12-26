def triple(lst):
    return lst**3

li = [1,2,3,4,5,6,7,8,9]
print(list(triple(i) for i in li))



from functools import reduce
def add(x,y):
    return x+y

print(reduce(add,[1,2,3,4,5,6,7,8,9]))
print(reduce(lambda x,y: x+y,[1,23,4,5,6]))


def my_gen(num):
    x = open('note.txt','r')
    while 1:
        yield x.read(num)

g = my_gen(15)
print(next(g))
print(next(g))

def has_null_value(lst):
    if lst:
        print("true")
    else:
        print("false")
has_null_value(1)

lann = []
def has_null_value1(lst):
    if len(lst):
        print("true")
    else:
        print("false")
has_null_value1(lann)


def fibonacci(a):
    if a ==  1 or a == 2:
        return 1
    elif a == 0:
        return 0
    else:
        return fibonacci(a-2) + fibonacci(a-1)
l = []
for a in range(10):
    l.append(fibonacci(a))
print(l)

import re, random, string
count1 = int(input('请输入密码个数(必须大于0)： '))
i = 0
passwds = []
while i < count1:
    tmp = random.sample(string.ascii_letters + string.digits, 8)
    passwd = ''.join(tmp)
    if re.search('[0-9]', passwd) and re.search('[A-Z]', passwd) and re.search('[a-z]', passwd):
        passwds.append(passwd)
        i += 1
print(passwds)


from functools import partial
def mul_by_two(*args):
    s = 2
    for n in args:
        s = s * n
    return s

a = partial(mul_by_two)
print(mul_by_two(20))


from functools import wraps
import time
def func_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        print
        '[Function: {name} start...]'.format(name=function.__name__)
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print
        '[Function: {name} finished, spent time: {time:.2f}s]'.format(name=function.__name__, time=t1 - t0)
        return result
    return function_timer
@func_timer
def test(x, y):
    s = x + y
    time.sleep(1.5)
    print('the sum is: {0}'.format(s))
if __name__ == '__main__':
    test(1, 2)
