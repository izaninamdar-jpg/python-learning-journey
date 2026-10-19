# String example: strings are immutable in Python
word = "python"
word = "J" + word[1:]
print(word)

# Name length example
name = input("enter your name ")
print("length of your name is", len(name))

# Conditional statements
age = int(input("enter the age"))
if age >= 18:
    print("can vote")
else:
    print("cant vote")

light = "green"
if light == "green":
    print("go")
elif light == "red":
    print("stop")
else:
    print("let the walkers go")

marks = int(input("enter total marks"))
if marks >= 90:
    print("A")
elif 80 <= marks < 90:
    print("B")
elif 70 <= marks < 80:
    print("C")
else:
    print("D")

# Nested conditions
age = int(input("enter the age"))
if age >= 18:
    if age >= 80:
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")
    if age <= 16:
        print("kyu nakhre hore")

num = int(input("enter the number"))
num2 = int(input("enter the second one"))
num3 = int(input("enter the third one"))
if num >= num2 and num >= num3:
    print("largest number is ", num)
elif num2 >= num and num2 >= num3:
    print("largest num is ", num2)
else:
    print("largest num is ", num3)

a = int(input("enter the number"))
if a % 7 == 0:
    print("its multiple of 7")
else:
    print("its not multiple")

string = input("enter the string")
substr = input("enter the substring")
print(string.find(substr))
