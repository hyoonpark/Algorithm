for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    chr_box = [[0 for _ in range(N)] for _ in range(N)]
    ans = 0
    for n in range(N):
        chr_box[n] = list(map(int, input().split()))
    for i in range(N):
        cnt = 0
        for j in range(N):
            if chr_box[i][j]:
                cnt += chr_box[i][j]
        if cnt == K:
            

