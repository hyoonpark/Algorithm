for tc in range(1, int(input())+1):
    t, p = map(str, input().split())
    N = len(t)
    M = len(p)
    i = 0
    cnt = 0
    while i < N:
        if t[i] == p[0]:
            if t[i:i+M] == p:
                cnt += 1
                i += M
            else:
                cnt += 1
                i += 1
        else:
            cnt += 1
            i += 1
    print(f'#{tc}', cnt)