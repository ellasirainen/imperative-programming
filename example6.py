low = 0
high = 0
for n in range(51):
    val = n*(n - 30)*(n - 50)
    if val > high:
        high = val
    if val < low:
        low = val

print(low, high)