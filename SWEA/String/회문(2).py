for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    chr_lst = [['' for _ in range(N)] for _ in range(N)]
    c = M//2
    char = ''
    for n in range(N):
        chr_lst[n] = list(input())
    if N == M:
        for i in range(N):
            char1 = ''
            char2 = ''
            for j in range(c):
                char1 += chr_lst[i][j]
            for j in range(N-1, N-c-1, -1):
                char2 += chr_lst[i][j]
            if char1 == char2:
                for m in range(M):
                    char += chr_lst[i][m]
                print(f'#{t}', char)
                break
        for j in range(N):
            char1 = ''
            char2 = ''
            for i in range(c):
                char1 += chr_lst[i][j]
            for i in range(N-1, N-c-1, -1):
                char2 += chr_lst[i][j]
            if char1 == char2:
                for m in range(M):
                    char += chr_lst[m][j]
                print(f'#{t}', char)
                break
    else:
        for i in range(N):
            for y in range(N - M):
                char = ''
                for j in range(y, y + M):
                    char += chr_lst[i][j]
                if char[:] == char[::-1]:
                    print(f'#{t}', char)
                    break