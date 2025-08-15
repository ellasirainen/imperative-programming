n = int(input('please give n: '))

if n <= 0:
    print('ERROR: not a positive value:' , n)
else:
    result = 1
    while n > 1:
        result *= n
        n -= 1

    print(result)
 