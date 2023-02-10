T = int(input())
for t in range(1, T+1):
    N = int(input())
    mrx = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 1
    r_srt = 0
    r_end = N - 1
    c_srt = 0
    c_end = N - 1
    while c_srt <= c_end and r_srt <= r_end:
        for i in range(c_srt, c_end+1):
            mrx[r_srt][i] = cnt
            cnt += 1
        r_srt += 1
        for i in range(r_srt, r_end+1):
            mrx[i][c_end] = cnt
            cnt += 1
        c_end -= 1
        for i in range(c_end, c_srt-1, -1):
            mrx[r_end][i] = cnt
            cnt += 1
        r_end -= 1
        for i in range(r_end, r_srt-1, -1):
            mrx[i][c_srt] = cnt
            cnt += 1
        c_srt += 1
    print(f'#{t}')
    for m in range(N):
        print(*mrx[m])