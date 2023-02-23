di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def Move(i, j):
    global cnt_dict, cnt
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<N:
            if room[ni][nj] == room[i][j] + 1:
                cnt += 1
                Move(ni, nj)
    cnt_dict[room[i][j]] = cnt



for tc in range(1, int(input())+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    cnt_dict = {}
    for i in range(N):
        for j in range(N):
            cnt = 1
            Move(i, j)
    ans1 = max(cnt_dict, key=cnt_dict.get)
    ans2 = cnt_dict.get(ans1)
    print(f'#{tc}', ans1, ans2)