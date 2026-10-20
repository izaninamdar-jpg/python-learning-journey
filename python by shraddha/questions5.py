"""n = int (input('enter the number '))
i = 1 
while i <= 10:
    print(n*i)
    i = i +1 
a = [1,4,9,16,25,36,49,64,81,100]
i = 0 
while i != len(a):
    print(a[i])
    i = i + 1

b = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0 
x = 36

while i != len(b):
    if b[i] == x:
        print('element found at index ', i)
        print('found')
    i = i + 1

list = (1,4,9,16,25,36,49,64,81,100)
for i in list:
    print(i)
    if (i == 36):
        print('found')
        break
n = int (input('enter the number '))
for i in range(n, n*10+1, n):
     print(i)" 
     int(input('enter the number'))
i =0
sum =0
while (i !=n):
    sum += i 
    i = i + 1 

print(sum)"""
m = int(input('enter the numbers'))
factorial = 1
for i in range(2,m+1,1):
    factorial = i * factorial 
print(factorial)
        
