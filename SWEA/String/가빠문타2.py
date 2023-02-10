def strSearch(t, p):
    N = len(t)
    M = len(p)
    i = 0
    j = 0
    cnt = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i -= j
            j = -1
        j += 1
        i += 1
        if j == M:
            cnt += 1
            j = 0
            i += M
    return N + cnt - (cnt*M)

for tc in range(1, int(input())+1):
    t, p = map(str, input().split())
    print(f'#{tc}', strSearch(t, p))