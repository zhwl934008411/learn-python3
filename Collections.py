from collections import namedtuple, deque,Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

# nametuple是一个函数,可以创建一个自定义的tuple对象,并且规定了tuple元素的个数
# 并可以通过属性访问tuple的元素

print(isinstance(p, tuple))
print(isinstance(p, Point))

Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
# append(),appendleft()/popleft()-->添加或删除头部的元素
q = deque(['a', 'b', 'c'])
q.append('x') #默认添加到末尾
q.pop()#默认删除尾部的元素
q.appendleft('d')
print(q)

#Counter 简单的计数器
c=Counter()
for ch in 'programing':
    c[ch] = c[ch]+1

print(c)



