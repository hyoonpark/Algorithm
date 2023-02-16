def mazeAns():
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    S = []
    S.append([row, col]) # 입구이동
    maze[row][col] = 1 # 방문표시
    while S:
        n = S.pop() # 갈 수 있는 좌표 꺼내기
        for k in range(4):
            ni = n[0] + dx[k]
            nj = n[1] + dy[k]
            if 0<=ni<N and 0<=nj<N: # 미로 내에서
                if maze[ni][nj] == '3':
                    return 1
                    break
                elif maze[ni][nj] == '0':
                    S.append([ni, nj])
                    maze[n[0]][n[1]] = 1 # 방문표시
    return 0 # 출구에 가지 못하고 모든칸 방문




for t in range(1, int(input())+1):
    N = int(input())
    maze = [list(input()) for i in range(N)]
    for i in range(N):
        if '2' in maze[i]:
            row = i
            col = maze[i].index('2')

    print(f'#{t}', mazeAns())