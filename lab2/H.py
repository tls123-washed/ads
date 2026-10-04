import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    k = int(data[1])
    words = data[2:]

    # Срез: берем элементы с k-го до конца, затем элементы с 0 по (k-1)
    shifted = words[k:] + words[:k]

    print(*shifted)

if __name__ == '__main__':
    main()