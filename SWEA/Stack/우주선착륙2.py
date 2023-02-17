di = [-1,1,0,0,-1,1,1,-1]
dj = [0,0,1,-1,1,1,-1,-1]

def Spare(lst, N, M):
    ans = 0

    for i in range(N):
        for j in range(M):
            cnt = 0  # 낮은 구역의 갯수 카운트
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<M:
                    if num_lst[i][j] > num_lst[ni][nj]:
                        cnt += 1
                        if cnt >= 4:
                            ans += 1
                            break

    return ans



for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    num_lst = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc}', Spare(num_lst, N, M))