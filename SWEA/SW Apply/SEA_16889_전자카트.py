def perm(i, k):
    global S
    if i == k:
        S.append([0]+p[:]+[0])
        # print(p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            perm(i+1, k)
            p[i], p[j] = p[j], p[i]


for tc in range(1, int(input())+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    p = []
    S = []
    ans = 1000
    for n in range(1, N):
        p.append(n)
    perm(0, N-1)
    for s in S:
        cnt = 0
        for i in range(N):
            cnt += area[s[i]][s[i+1]]
        if ans >= cnt:
            ans = cnt

    print(f'#{tc}', ans)