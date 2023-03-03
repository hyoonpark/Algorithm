C, R = map(int, input().split())
K = int(input())
seat = [[0]*C for _ in range(R)]
cnt = 1
r_srt = 0
r_end = R-1
c_srt = 0
c_end = C-1
if K > C*R:
    print(0)
else:
    while r_srt <= r_end and c_srt <= c_end:
        for i in range(r_srt, r_end+1):
            if K >= cnt:
                seat[i][c_srt] = cnt
                cnt += 1
            else:
                break
        c_srt += 1
        for i in range(c_srt, c_end+1):
            if K >= cnt:
                seat[r_end][i] = cnt
                cnt += 1
            else:
                break
        r_end -= 1
        for i in range(r_end, r_srt-1, -1):
            if K >= cnt:
                seat[i][c_end] = cnt
                cnt += 1
            else:
                break
        c_end -= 1
        for i in range(c_end, c_srt-1, -1):
            if K >= cnt:
                seat[r_srt][i] = cnt
                cnt += 1
            else:
                break
        r_srt += 1
    for j in range(R):
        if K in seat[j]:
            y = j
            x = seat[y].index(K)
            print(x+1, y+1)
            break
