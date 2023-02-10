T = int(input())

for i in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_gravity = []
    for j in range(N):
        counts = 0
        for k in range(j + 1, N):
            if numbers[j] > numbers[k]:
                counts += 1
            max_gravity.append(counts)

    num_max = max_gravity[0]

    for y in max_gravity:
        if y > num_max:
            num_max = y

    print(f'#{i} {num_max}')
