for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    chr_lst = ['' for _ in range(N)]
    for n in range(N):
        chr_lst[n] = input()
    # if N < M:
    #     for i in range(N):
    #         char = ''
    #         for j in range(M):
    #             char += chr_lst[i][j]
    #         if char[:] == char[::-1]:
    #             print(f'#{t}', char)
    #             break
    #     for j in range(N):
    #         char = ''
    #         for i in range(M):
    #             char += chr_lst[i][j]
    #         if char[:] == char[::-1]:
    #             print(f'#{t}', char)
    #             break
    # else:
    for i in range(N):
        for y in range(N-M+1):
            char = ''
            for j in range(y, y+M):
                char += chr_lst[i][j]
            if char[:] == char[::-1]:
                print(f'#{t}', char)
                break
    for j in range(N):
        for x in range(N-M+1):
            char = ''
            for i in range(x, x+M):
                char += chr_lst[i][j]
            if char[:] == char[::-1]:
                print(f'#{t}', char)
                break

