def strSearch(t, p):
    M = len(p)
    N = len(t)
    cnt = 0
    i = 0
    for _ in range(N -M +1):
        flag = False
        if t[i] == p[0]:
            flag = True
            for j in range(M):
                if t[i + j] != p[j]:
                    flag = False
                    i += 1
                    break
        if flag:
            cnt += 1
            i += M
    return N + cnt - (cnt*M)

for tc in range(1, int(input())+1):
    t, p = map(str, input().split())
    print(f'#{tc}', strSearch(t, p))