s = int(input('please give the value of s: '))

n = 1
found = False

while found == False:
    if n*(n + 1) / 2 > s:
        found = True
    else:
        n += 1

print(n)