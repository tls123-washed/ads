class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

n = int(input())
values = list(map(int, input().split()))

# Создаем связный список
head = Node(values[0])
current = head
for val in values[1:]:
    current.next = Node(val)
    current = current.next

# Удаляем каждый второй узел
current = head
while current and current.next:
    current.next = current.next.next
    current = current.next

# Собираем и выводим результат
result = []
current = head
while current:
    result.append(current.val)
    current = current.next

print(*result)