def bubble_sort(alist):
    for j in range(len(alist)-1):
        for i in range(j):

            if alist[i] > alist[i+1]:

                alist[i], alist[i+1] = alist[i+1], alist[i]

li = [54,26,93,17,77,31,44,55,20]
bubble_sort(li)
print(li)