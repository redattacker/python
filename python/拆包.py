def run(a, *args):
    # 第一个参数传给了a
    print(a)
    # args是一个元组，里面是2和3两个参数
    print(args)
    # *args是将这个元组中的元素依次取出来
    print("对args拆包")
    print(*args)  # *args 相当于 a,b = args
    print("将未拆包的数据传给run1")
    run1(args)
    print("将拆包后的数据传给run1")
    run1(*args)


def run1(*args):
    print("输出元组")
    print(args)
    print("对元组进行拆包")
    print(*args)


run(1, 2, 3,)


# def run(**kwargs):  # 传来的 key = value 类型的实参会映射成kwargs里面的键和值
#     # kwargs是一个字典，将未命名参数以键值对的形式
#     print(kwargs)
#     print("对kwargs拆包")
#     #  此处可以把**kwargs理解成对字典进行了拆包，{"a":1,"b":2}的kwargs字典又
#     # 被拆成了a=1,b=2传递给run1,但是**kwargs是不能像之前*args那样被打印出来看的
#     run1(**kwargs)
#     print(*kwargs)
#
#
# def run1(a, b):  # 此处的参数名一定要和字典的键的名称一致
#     print(a, b)
#
#
# run(a=1, b=2)
