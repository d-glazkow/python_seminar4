import random 
a = int(input('введите длину массива - '))
lst = []
for i in range (a):
    b = random.randint(0,10)
    lst.append(b)
print(lst)
for i in range(a):
    f = True
    for j in range(a):
        if lst[i] == lst[j] and i != j:
            f = False
            break
    if f == True:
        print(lst[i],end=' ')