for _ in range(1, 11):
    tc = int(input())
    p = input()
    t = input()
    cnt = 0
    for i in range(len(t)):
        if t[i] == p[0]:
            if t[i:i+len(p)] == p:
                cnt += 1
    print(f'#{tc}', cnt)