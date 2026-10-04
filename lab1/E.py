n = int(input())
output = []
divisor = 2
while divisor * divisor <= n:
    while n % divisor == 0:
        output.append(divisor)
        n //= divisor
    divisor += 1
if n > 1:
    output.append(n)
print(*output)