highest= 0
time = 0
for t in range(101):
    previous = (t-1)*(t - 1 - 20)*(t - 1 - 100) + 120000
    now = t*(t - 20)*(t - 100) + 120000
    
    decrease = previous - now
    if decrease > highest:
        highest = decrease
        time = t

print(time)
