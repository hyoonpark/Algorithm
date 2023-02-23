di = [0, 0, -1, 1, -1, 1, 1, -1]    # 여덟 방향 델타 이동
dj = [-1, 1, 0, 0, 1, 1, -1, -1]
def Check(lst, N, M):
    ans = 0

    for i in range(N):
        for j in range(M):    # 열이 옮겨질 때마다 초기화
            cnt = 0
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<M:    # 각 방향이 유효한지
                    if lst[i][j] > lst[ni][nj]:    # 문제 조건에 맞게
                        cnt += 1
                        if cnt >= 4:
                            ans += 1
                            break

    return ans



for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    bu_lst = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc}', Check(bu_lst, N, M))