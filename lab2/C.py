import sys

def main():
    # Читаем абсолютно ВЕСЬ ввод (все строки целиком)
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    names = data[1:]

    result = []

    for name in names:
        if not result or name != result[-1]:
            result.append(name)

    print(len(result))
    print('\n'.join(result))

if __name__ == '__main__':
    main()