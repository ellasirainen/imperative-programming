#1
a = int(input('give value a: '))
b = int(input('give value b: '))

if a <= 100 or b >= 50:
    print(1)
else:
    print(0)
#2
if a <= 100 or b <= 100 and a >= 50 or b >= 50:
    print(1)
else:
    print(0)