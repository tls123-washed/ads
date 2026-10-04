import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    line1 = list(map(int, lines[0].split()))
    n = line1[0]
    vals1 = line1[1:] if n > 0 else []

    line2 = list(map(int, lines[1].split()))
    m = line2[0]
    vals2 = line2[1:] if m > 0 else []

    merged = sorted(vals1 + vals2)
    
    if merged:
        print(*merged)
    else:
        print()

if __name__ == '__main__':
    main()