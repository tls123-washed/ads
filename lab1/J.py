from collections import deque

boris = deque(map(int, input().split()))
nursik = deque(map(int, input().split()))

moves = 0

while boris and nursik:
    b = boris.popleft()
    n = nursik.popleft()

    if (b == 0 and n == 9) or (b > n and not (b == 9 and n == 0)):
        boris.append(b)
        boris.append(n)
    else:
        nursik.append(b)
        nursik.append(n)

    moves += 1

if boris:
    print("Boris", moves)
else:
    print("Nursik", moves)