from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    letters = input().split()

    count = {}
    queue = deque()
    result = []

    for char in letters:
        count[char] = count.get(char, 0) + 1
        queue.append(char)

        while queue and count[queue[0]] > 1:
            queue.popleft()

        if queue:
            result.append(queue[0])
        else:
            result.append(-1)

    print(*result)