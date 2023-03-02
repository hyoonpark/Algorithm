def Paint(i):
    global cnt
    cnt_w = 0
    cnt_b = 0
    cnt_r = 0
    if i == 0:
        cnt_w = flg[i].count('W')
        cnt += (M-cnt_w)
        i += 1
        Paint(i)
    elif i == M-1:
        cnt_r = flg[i].count('R')
        cnt += (M-cnt_r)
        return



for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    flg = [list(input()) for _ in range(N)]
    cnt = 0
    Paint(0)
    print(f'#{tc}', cnt)