v = 9
while v <= 65:
    print(v, end=' ')
    v += 4
print()


v = 3
for i in range(13): 
    print(v, end=' ')
    v *= 2
print()

for v in range(1,41):
    if v % 4 == 0:
        x = -1
    else:
        x = v
    print(x, end=' ')
