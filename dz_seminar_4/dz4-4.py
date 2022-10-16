import random
a = int(input('введите натуральную степень k - '))
for i in reversed(range(a)):
    if i > 1:
        b = random.randint(2, 10)
        print(b,'x^',i,'+ ',end ='')
        if i == 1:
            b = random.randint(2, 10)
            print(b,'x','+',end ='')
            if i == 0:
                b = random.randint(2, 10)
                print(b,'=0',end ='')
            else:
                break
b = random.randint(2, 10)
print(b,'x+',end ='')
b = random.randint(2, 10)
print(b,'=0',end ='')