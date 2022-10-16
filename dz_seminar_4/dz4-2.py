n = int(input("введите натуральное число N: "))
i=2
number = []
while i * i < n:
    while n % i == 0:
        number.append(i)
        n = n / i
    i = i + 1
if n > 1:
    number.append(n) 
print (number)