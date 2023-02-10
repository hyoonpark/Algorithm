for _ in range(1, 11):
    t = int(input())
    ladder = [[0 for _ in range(100)] for _ in range(100)]
    min_num = 10001
    min_idx = 0
    for n in range(100):
        ladder[n] = list(map(int, input().split()))
    for j in range(100):
        cnt = 0
        idx = j
        if ladder[0][j]:
            for i in range(100):
                cnt += 1
                if j > 0 and ladder[i][j - 1]:
                    while j > 0 and ladder[i][j - 1] == 1:
                        j -= 1
                        cnt += 1
                elif j < 99 and ladder[i][j + 1]:
                    while j < 99 and ladder[i][j + 1] == 1:
                        j += 1
                        cnt += 1
            if cnt <= min_num:
                min_num = cnt
                min_idx = idx
    print(f'#{t}', min_idx)