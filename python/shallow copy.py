from functools import reduce
# import copy
# a=[1,2,3,4,5,[3,4,[45,4]]]
# b=copy.copy(a)
# print(a)
# print(id(x) for x in a)
# print(b)
# print(id(x) for x in b)
# a[2]=1
# a[5][2][0]=34
# print(a)
# print(b)
# print(isinstance(round(15.5),float))
# print(11 < 'test')
# d={'a':24,'g':52,'i':12,'k':33}
# print(sorted(d.items(),key = lambda x:x[1]))
# print([d[i] for i in d if d[i]==12])
# print([] is not None)
# print({i:d[i] for i in d})
# d=[{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
# print(sorted(d,key = lambda x:x['age']))
# def a(e=3):
#     print(e)
# a(4)
print(list(reduce(lambda x: x, [y for y in range(3)])))
print(reduce(lambda x, y: x+y, [1,2,3,4,5]))