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
    """
b = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0 
x = 36

while i != len(b):
    if b[i] == x:
        print('element found at index ', i)
        print('found')
    i = i + 1
