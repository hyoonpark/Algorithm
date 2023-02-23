for _ in range(1, 11):
    t = int(input())
    ladder = [[0 for _ in range(102)] for _ in range(102)]
    for n in range(100):
        ladder[n+1] = list(map(int, input().split()))
    j = 0
    while ladder[100][j] != 2:
        j += 1
    for i in range(99, 1, -1):
        if ladder[i][j+1]:
            while ladder[i][j+1] != 0:
                j += 1
        elif ladder[i][j-1]:
            while ladder[i][j-1] != 0:
                j -= 1
    print(j)