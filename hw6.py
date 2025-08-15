w = int(input('give integer: '))
if w <= 2:
    p = 3
elif w > 2 and w <= 5:
    p = 3 
    for i in range(2,w):
        p += 2
else:
    p = 9 #price of posting 5 kg
    for v in range(5,w):
        p += 3
print (p)
