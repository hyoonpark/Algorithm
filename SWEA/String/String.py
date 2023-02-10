def strSearch(t, p):
    M = len(p)
    N = len(t)
    cnt = 0
    for i in range(N - M + 1):
        flag = False
        if t[i] == p[0]:
            flag = True
            for j in range(M):
                if t[i + j] != p[j]:
                    flag = False
                    break
        if flag:
            cnt += 1
    return cnt

for _ in range(1, 11):
    tc = int(input())
    p = input()
    t = input()
    print(f'#{tc}', strSearch(t, p))