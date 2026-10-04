s1 = input()
s2 = input()

result1 = []
result2 = []

for char in s1:
    if char != "#":
        result1.append(char)
    elif result1:
        result1.pop()

for char in s2:
    if char != "#":
        result2.append(char)
    elif result2:
        result2.pop()

if result1 == result2:
    print("Yes")
else:
    print("No")