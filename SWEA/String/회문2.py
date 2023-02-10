for _ in range(10):
    t = int(input())
    chr_lst = ['' for _ in range(N)]
    for n in range(N):
        chr_lst[n] = input()
    for i in range(N):
        for y in range(N-M+1):
            char1 = ''
            for j in range(y, y+M):
                char1 += chr_lst[i][j]
            if char1[:] == char1[::-1]:
                chr_len

    for j in range(N):
        for x in range(N-M+1):
            char2 = ''
            for i in range(x, x+M):
                char2 += chr_lst[i][j]
            if char2[:] == char2[::-1]:
                print(f'#{t}', char)
                break