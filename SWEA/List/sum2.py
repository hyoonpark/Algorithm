for t in range(1, 11):
    tc = int(input())
    num_lst = [[0for _ in range(100)] for _ in range(100)]
    sum_lst1 = []
    sum_lst2 = []
    max_lst = []
    for n in range(100):
        num_lst[n] = list(map(int, input().split()))
    for i in range(100):
        sum_num = 0
        for j in range(100):
            sum_num += num_lst[i][j]
            if j == 99:
                sum_lst1.append(sum_num)
        max_lst.append(max(sum_lst1))
    for j in range(100):
        sum_num = 0
        for i in range(100):
            sum_num += num_lst[i][j]
            if i == 99:
                sum_lst2.append(sum_num)
        max_lst.append(max(sum_lst2))
    sum_num = 0
    for i in range(100):
        sum_num += num_lst[i][i]
    max_lst.append(sum_num)
    sum_num = 0
    for i in range(100):
        for j in range(99, -1, -1):
            if i + j == 99:
                sum_num += num_lst[i][j]
    max_lst.append(sum_num)
    print(f'#{t}', max(max_lst))



