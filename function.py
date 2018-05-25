# -*- coding:utf-8 -*-

import math


class function(object):
    def __init__(self, r, a, b, c):
        self.r = r
        self.a = a
        self.b = b
        self.c = c

    def __area_of_circle__(self):
        S = math.pi * (self.r) * (self.r)
        return S

    def __abs__(self):
        if not isinstance(self.r, (int, float)):
            raise TypeError('bad operand type ')
        if self.r >= 0:
            return self.r
        else:
            return -self.r

    def __quadratic__(self):
        x = math.sqrt((self.b * self.b) - 4 * self.a * self.c)
        x1 = (-self.b + x) / (2 * self.a)
        x2 = (-self.b - x) / (2 * self.a)
        return x1, x2

    def __power__(self):
        return self.r * self.r

    def __power3__(self, n):
        s = 1
        while n > 0:
            n = n - 1
            s = s * self.r
        return s

    def __power4__(self, n=5):
        s = 1
        while n > 0:
            n = n - 1
            s = s * self.r
        return s

    def __add_end__(self, L=[]):
        L.append('END')
        return L

    def __add_end2__(self, L=None):
        if L is None:
            L = []
        L.append('END')
        return L

    def __calc__(self, numbers):  # 将list或tuple作为函数的参数
        sum = 0
        for n in numbers:
            sum = sum + n * n
        return sum

    def __calc2__(self, *numbers):  # 将函数的参数作为可变参数
        sum = 0
        for n in numbers:
            sum = sum + n * n
        return sum

    def __person__(self, name, age, **kwargs):

        if 'city' in kwargs:
            print('pass')
        if 'job' in kwargs:
            print('pass')
        # return None
        print('name:', name, 'age:', age, 'other', kwargs)

    def __person2__(self, name, age, *, city, job):
        print('name:', name, 'age:', age, 'city:', city, 'job:', job)

    def __person3__(self, name, *, city='Beijing', job):
        print(name, city, job)

    def __f1__(self, a, b, c=0, *args, **kwargs):
        print('a=', a, 'b=', b, 'c=', c, 'args:', args, 'kwargs=', kwargs)

    def __f2__(self, a, b, c=0, *, d, **kwargs):
        print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kwargs=', kwargs)

    def product(self, *args):
        S = 1
        if len(args) == 0:
            return S
        else:
            for arg in args:
                S = S * arg
            return S

    def __fact__(self, n):

        if n == 0:
            return 1
        else:
            S = 1
            while n > 0:
                S = S * n
                n = n - 1
            return S

    def __trim__(self, s):  # 去除首尾的空格
        if s[:1] == ' ':
            s = s[1:]
        if s[-1:] == ' ':
            s = s[:-1]
        d = {'a': 1, 'b': 2, 'c': 9}
        for key in d:
            print(key)
        for value in d.values():
            print(value)
        for k, v in d.items():
            print(k, ':', v)
        return s


if __name__ == '__main__':
    s1 = function(2, 2, 3, 1)
    # print(s1.__area_of_circle__())
    # print(s1.__abs__())
    # print(str(hex(255)))
    # print(str(hex(1000)))
    s2 = function(111, 1, 3, -4)
    '''if s1.quadratic() != (-0.5, -1.0):
        print("测试失败")
    elif s2.quadratic() != (1.0, -4.0):
        print("测试失败")
    else:
        print("测试成功")

    # print(math.sqrt(4))
    print(s1.__power3__(3))
    print(s1.__power4__(3))
    print(s1.__add_end__())
    print(s1.__add_end__())
    print(s1.__add_end__()) #原来的L没有重置
    print(s1.__add_end2__([1,2]))
    print(s1.__add_end2__())
    print(s1.__add_end2__())
    print(s1.__calc__([1,2,3,4]))
    print(s1.__calc2__(1,2,3,4))
    print(s1.__calc2__(1,2,3,4,5))
    nums=[1,2,3,4,5]
    print(s1.__calc2__(*nums)) #*表示nums元组的所有元素作为可变参数传入到函数
    s1.__person__('xiaoming',11,city='tianjin',country='China') #关键字参数将参数和参数值自动转化为dict输出
    extra = {'city':'Beijing','job':'Engineer'}
    s1.__person__('xiaohong',22,**extra)
    s1.__person2__('xiaolu',11,city='beijing',job='teacher')
    s1.__person3__('ciaokk',job='tyt')
    s1.__f1__(3,4)
    s1.__f1__(3,4,5)
    s1.__f1__(3,4,3,'ff2','ff',city='beijing',country='China')'''
    args = (1, 23, 4, 5, 4)
    args2 = (1, 34, 5)
    kwargs = {'d': 99, 'x': '#'}
    s1.__f1__(*args, **kwargs)
    s1.__f2__(*args2, **kwargs)


    def __test__():
        print('product(5)=', s1.product(5))
        print('product(5,6)=', s1.product(5, 6))
        print('product(5,6,7)=', s1.product(5, 6, 7))
        print('product(5,6,7,9)=', s1.product(5, 6, 7, 9))
        if s1.product(5) != 5:
            print('测试失败')
        elif s1.product(5, 6) != 30:
            print('测试失败')
        elif s1.product(5, 6, 7) != 210:
            print('测试失败')
        elif s1.product(5, 6, 7, 9) != 1890:
            print('测试失败')
        else:
            try:
                s1.product()
                print('测试成功')
            except TypeError:
                print('测试失败')


    # __test__()
    print(s1.__fact__(10))


    def __fact2__(n):
        if n == 1:
            return 1
        else:
            return n * __fact2__(n - 1)


    # print(__fact2__(999))#递归调用栈溢出
    print(s1.__trim__(' fj aaj '))
