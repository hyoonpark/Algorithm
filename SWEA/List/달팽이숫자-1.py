T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 1
    dalpang = [[0 for _ in range(N)] for _ in range(N)]  # 배열 0으로 초기화

    r_st = 0
    r_end = N - 1
    c_st = 0
    c_end = N - 1

    while c_st <= c_end and r_st <= r_end:
        for i in range(c_st, c_end + 1):  # 왼쪽에서 오른쪽
            dalpang[r_st][i] = cnt
            cnt += 1
        r_st += 1

        for i in range(r_st, r_end + 1):  # 위에서 아래
            dalpang[i][c_end] = cnt
            cnt += 1
        c_end -= 1

        for i in range(c_end, c_st - 1, -1):  # 오른쪽에서 왼쪽
            dalpang[r_end][i] = cnt
            cnt += 1
        r_end -= 1

        for i in range(r_end, r_st - 1, -1):  # 아래에서 위쪽
            dalpang[i][c_st] = cnt
            cnt += 1
        c_st += 1

    print(f'#{tc}')
    for i in range(N):
        print(*dalpang[i])