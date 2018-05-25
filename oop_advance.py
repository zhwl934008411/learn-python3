from types import MethodType


class Student(object):
    pass


xiaoli = Student()
xiaoli.name = 'xiaoli'  # 给实例绑定name属性
print(xiaoli.name)


def set_age(self, age):  # 给实例绑定方法
    self.age = age


xiaoli.set_age = MethodType(set_age, xiaoli)
