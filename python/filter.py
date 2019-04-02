def f1(x):
    if x > 20:
        return True
    else:
        return False


l1 = [1, 2, 3, 42, 67, 16]
print(filter(f1, l1))
# 输出如下：
# <filter object at 0x000000000117B898>
l2 = filter(f1, l1)
print(l2)
# 输出如下
# <filter object at 0x0000000000BCB898>
print(l2.__next__)
# 输出如下
# <method-wrapper '__next__' of filter object at 0x000000000074B898>
print(l2.__next__())
# 42
print(l2.__next__())
# 67
print(l2.__next__())
# 遍历结束出现异常
# Traceback (most recent call last):
#   File "<pyshell#14>", line 1, in <module>
#     l2.__next__()
# StopIteration  filter()为已知的序列的每个元素调用给定的布尔函数，调用中，返回值为非零的元素将被添加至一个列表中