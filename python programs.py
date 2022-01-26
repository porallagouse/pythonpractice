'''#01checking the given number id even number or not
n=int(input("Enter a number:"))
if n%2==0:
    print("it is a even number")
else:
    print("it is not a even number")

#check lower case or not
char=input("Enter a number:")
if char.islower():
    print(f"{char}it is a lower case")
else:
    print(f"{char}it is not a lower case")
'''
#greatest among 3 numbers
n1=10
n2=20
n3=30
if n1>n2 and n1>n3:
    print("n1 is greater")
elif n2>n3:
    print("n2 is greater")
else:
    print("n3 is greater")
#

char='a'
d={}
if char.lower() in "aeiou":
    #d[char]=ord(char)
    d.update({char:ord(char)})
print(d)

#
n=1
while n<=10:
    print(n)
    n+=1
#
n=10
while n>0:
    print(n)
    n-=1
#
n=-1
while n>=-10:
    print(n)
    n-=1
#
n = -10
while n <= -1:
    print(n)
    n += 1
#
n = 1
while n <= 50:
    if n % 2 == 0:
        print(n)
    n += 1
#
s = "gouse"
c = 0
while c < len(s):
    print(s[c])
    c += 1
#
t = (10, 20, 30, 40, 50)
c = 0
while c < len(t):
    print(t[c])
    c += 1
#
l = [1, 2, 3, 4, 5]
i = 0
while i < len(l):
    print(l[i])
    i += 1
#
for i in range(1, 100):
    print(i)
#
for i in range(-1, -11, -1):
    print(i)
#
for i in range(-10, 0, 1):
    print(i)
# even numbers
for i in range(0, 11, 2):
    print(i)
# odd numbers
for i in range(1, 11, 2):
    print(i)
#
s = "python"
for i in range(len(s)):
    print(s[i])
#
s = "python"
for char in s:
    print(char)
#
l = [1, 2, 3, 4, 5]
for i in range(len(l)):
    print(l[i])
#
#
d = {'one': 1, 'two': 2, 'three': 3}
for key in d:
    print()
#
s= 'hello'
for i in range(len(s)):
    print(s[i])


#
s = "hello"
for i in enumerate(s):
    print(i)
#
s ='hello'
for index,item in enumerate(s):
    print(index, "-->", item)
#
s="hai"
for i in range(len(s) -1, -1, -1):
    print(s[i])

#
s = "hai"
for i in s[::-1]:
    print(s)
#
s = "gouse"
count = 0
for i in s:
    count += 1
print(count)
#
s = "gouse"
for i in range(0, len(s), 2):
    print(s[i])
#
s="gouse"
for i in s[::2]:
    print(i)
#
s = "gouse 12345"
for char in s:
    if char.isdigit():
        print(char)
#
s = "gouse 12345"
count = 0
for char in s:
    if char.isdigit():
        count +=1
        print(char)
















