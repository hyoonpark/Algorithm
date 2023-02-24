T = 10

for i in range(1, T+1):
    dump = int(input())
    box_h = list(map(int, input().split()))
    for _ in range(dump):
        box_h[box_h.index(max(box_h))] -= 1
        box_h[box_h.index(min(box_h))] += 1

    sub = max(box_h) - min(box_h)
    print(f'#{i} {sub}')