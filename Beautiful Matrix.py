for r in range(1, 6):
    row = list(map(int, input().split()))
    if 1 in row:
        c = row.index(1) + 1
        print(abs(r - 3) + abs(c - 3))
        break
