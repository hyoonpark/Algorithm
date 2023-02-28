def check():
    # 오른쪽, 아래, 오른쪽 아래 대각선, 왼쪽 아래 대각선
    dx = [0, 1, 1, 1]
    dy = [1, 0, 1, -1]

    for i in range(n):
        for j in range(n):
            if omok[i][j] == 'o':
                for dir in range(4):
                    nx = i
                    ny = j
                    cnt = 0

                    while 0 <= nx < n and 0 <= ny < n and omok[nx][ny] == 'o':
                        cnt += 1
                        nx += dx[dir]
                        ny += dy[dir]
                    if cnt >= 5:
                        return 'YES'
    return 'NO'


for tc in range(1, int(input())+1):
    n = int(input())
    omok = [input() for _ in range(n)]

    ans = check()
    print(f'#{tc}', ans)
