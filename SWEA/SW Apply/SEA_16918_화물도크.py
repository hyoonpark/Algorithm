for tc in range(1, int(input())+1):
    N = int(input())
    sch = [list(map(int, input().split())) for _ in range(N)]

    sch.sort(key=lambda x: (x[1], x[0]))
    cnt = 1
    now = sch[0][1]
    for i in range(1, N):
        s = sch[i][0]
        if now <= s:
            cnt += 1
            now = sch[i][1]
    print(f'#{tc}', cnt)


    # print(s, e)
    # print(sch)