from collections import *


class FloatList(UserList):
    def append(self, obj):
        if type(obj) == float:
            self.data.append(obj)

    def __setitem__(self, key, value):
        if type(value) == float:
            self.data[key] = value

    def __add__(self, digit):
        if type(digit) == float:
            super(FloatList, self).append(digit)


f_list = FloatList()

f_list.append('5')
print(f_list)
f_list.append(5.4)  # [5.4]
print(f_list)
f_list.__setitem__(0, 7.0)
f_list.append(6.0)  # [5.4, 6.0]
print(f_list)
s_f_list = f_list + 7.8  # s_f_list [5.4, 6.0, 7.8], f_list [5.4, 6.0]
print(s_f_list)
