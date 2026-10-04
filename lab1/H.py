n = int(input())
a = list(map(int, input().split()))

result = []
stack = []

for age in a:
    while stack and stack[-1] >= age:
        stack.pop()
    if stack:
        result.append(stack[-1])
    else:
        result.append(-1)
    stack.append(age)
print(*result)