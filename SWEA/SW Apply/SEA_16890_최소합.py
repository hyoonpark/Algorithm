def DFS(x, y):
    # 전역변수 선언
    global min_total, sub_sum
    # 더 계산할 필요가 없다.
    if min_total < sub_sum:
        return
    # x,y가 N-1, N-1 즉 목적지에 도달하면 종료
    if x == N-1 and y == N-1:
        if min_total > sub_sum:
            min_total = sub_sum
    # 아래, 오른쪽으로만 진행 가능
    dx, dy = [1,0], [0,1]
    for i in range(2):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<N and 0<=yy<N and not visited[xx][yy]:
            visited[xx][yy] = True
            sub_sum += maze[xx][yy]
            DFS(xx,yy)
            visited[xx][yy] = False
            sub_sum -= maze[xx][yy]


for tc in range(1, int(input())+1):
    N = int(input())
    maze = [list(map(int, input().split())) for _ in range(N)]
    # N의 최대값은 13이고 10 이하의 자연수 이므로 합이 260을 넘을 수 없다.
    min_total = 260
    # 부분합 계산
    sub_sum = maze[0][0]
    # 방문한 위치 체크
    visited = [[False for _ in range(N)] for i in range(N)]
    # 0,0에서 출발
    DFS(0, 0)
    print(f'#{tc}', min_total)