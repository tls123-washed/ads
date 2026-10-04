n = int(input())

number = 1
count = 0

while count < n:
    number += 1
    is_prime = True
    divisor = 2
    
    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
    divisor += 1
    
    if is_prime:
        count += 1
    
print(number)