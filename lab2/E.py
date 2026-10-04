import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    values = data[1:]

    # Крайний случай: один элемент — вывод пустой
    if n == 1:
        print()
        return

    # 1. Построение односвязного списка
    head = Node(values[0])
    curr = head
    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next

    # 2. Удаление центрального узла (индекс n // 2)
    target_idx = n // 2
    curr = head
    for _ in range(target_idx - 1):
        curr = curr.next

    # Перешагиваем через удаляемый узел
    curr.next = curr.next.next

    # 3. Сбор остатка списка
    result_list = []
    curr = head
    while curr:
        result_list.append(curr.val)
        curr = curr.next

    # 4. Вывод
    print(*result_list)

if __name__ == '__main__':
    main()