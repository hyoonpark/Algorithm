for i in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0
    for j in range(2, N - 1):
        for k in range(1, buildings[j] + 1):
            if k > buildings[j - 2] and k > buildings[j - 1] and k > buildings[j + 2] and k > buildings[j + 1]:
                cnt += 1

    print(f'#{i} {cnt}')