n = int(input('please give n: '))

if n <= 0:
    print('ERROR: not a positive value:' , n)
else:
    result = 1
    for i in range(2, n+1):
        result *= i
    
    print(result)