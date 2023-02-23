for _ in range(1, 11):
    t = int(input())
    ladder = [[0 for _ in range(100)] for _ in range(100)]
    for n in range(100):
        ladder[n] = list(map(int, input().split()))
    j = 0
    while ladder[99][j] != 2:
        j += 1
    for i in range(98, 0, -1):
        if j < 99 and ladder[i][j+1]:
            while j < 99 and ladder[i][j+1] == 1:
                j += 1
        elif j > 0 and ladder[i][j-1]:
            while j > 0 and ladder[i][j-1] == 1:
                j -= 1
    print(f'#{t}', j)