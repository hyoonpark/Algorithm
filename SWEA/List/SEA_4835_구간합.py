# 1
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

# 2
for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    num_lst = list(map(int, input().split()))
    add_num = 0
    sum_max = 0
    sum_min = 1000001
    for i in range(N-M+1):
        add_num = 0
        for j in range(i, i+M):
            add_num += num_lst[j]
        if add_num > sum_max:
            sum_max = add_num
        if add_num < sum_min:
            sum_min = add_num
    print(f'#{t}', sum_max-sum_min)