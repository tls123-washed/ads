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
    
    # 1. Построение односвязного списка
    head = Node(values[0])
    curr = head
    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next
        
    # 2. Разворот связного списка (переворачиваем указатели next)
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # Сохраняем следующий узел
        curr.next = prev       # Разворачиваем указатель
        prev = curr            # Сдвигаем prev вперед
        curr = next_node       # Сдвигаем curr вперед
        
    head = prev  # Новый голова списка
    
    # 3. Обход развернутого списка и вывод
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
        
    print(*result)

if __name__ == '__main__':
    main()