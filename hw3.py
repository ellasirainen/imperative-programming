#1
i = 10
while i <= 37:
    print(i, end=' ')
    i += 3
print()
#2

v = 998
while v >= 900:
    print(v, end=' ')
    v -= 2
print()
#3

for v in range(20):
    if v % 2 == 0:
        x = 1
    else:
        x = -1
    print(x, end=' ')
print()
#4

for i in range(60):
    if i % 3 == 0 or i % 3 == 1:
        n = 7
    else:
        n = 9
    print(n, end=' ')
