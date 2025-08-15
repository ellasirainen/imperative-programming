#1
a = int(input('Give a nonnegative integer a: '))
n = 3
for i in range(1,a):
    n *= 3
print(n)
print()

#2
b = int(input('Give an integer b: '))
for i in range(1,a):
    b *= a
print(b)