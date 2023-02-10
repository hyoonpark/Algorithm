T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    add_list = []
    for j in range(N-M+1):
        answer = 0
        for k in range(j, j+M):
            answer += numbers[k]
        add_list.append(answer)

    print(f'#{i} {max(add_list)-min(add_list)}')