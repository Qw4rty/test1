from random import randint
a = []
for i in range(10):
    a.append(randint(1, 50))
a.sort()
print(a)
def insertionSort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while a[j] > key and j >= 0:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a