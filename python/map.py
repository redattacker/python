#map()将函数调用映射到每个序列的对应元素上并返回一个含有所有返回值的列表
#
def f1( x, y ):
   return (x,y)

l1 = [ 0, 1, 2, 3, 4, 5, 6 ]
l2 = [ 'Sun', 'M', 'T', 'W', 'T', 'F', 'S' ]
l3 = map( f1, l1, l2 )
print(list(l3))
#[(0, 'Sun'), (1, 'M'), (2, 'T'), (3, 'W'), (4, 'T'), (5, 'F'), (6, 'S')]

def f2(x):
    return(x*2)
print( list(map(f2, l1)))
#[0, 2, 4, 6, 8, 10, 12]

print( list(map(f2, l2)))
# ['SunSun', 'MM', 'TT', 'WW', 'TT', 'FF', 'SS']

def f3( x, y ):
  return (x*2, y*2)
print( list(map(f3, l1, l2)))
# [(0, 'SunSun'), (2, 'MM'), (4, 'TT'), (6, 'WW'), (8, 'TT'), (10, 'FF'), (12, 'SS')]
