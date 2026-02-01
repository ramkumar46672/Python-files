def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = 56
print(is_prime(n)) 

i =1
j = 1
while True:
    c = n+i
    b = is_prime(c)
    i = i+1
    if b == True:
        print(c)
        break

  
while True:
    c = n-j
    b=is_prime(c)
    j = j+1
    if b == True:
        print(c)
        break
