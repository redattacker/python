import time
def timeit(func):
    print('1111')

    def wrapper():
        start = time.time()
        print('33')
        func()
        end =time.time()
        print ('used:', end - start)
    return wrapper
@timeit
def foo():
    sum=0
    for i in range(1000):
        sum+=i

    print(sum)

foo()