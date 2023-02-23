for t in range(1, int(input())+1):
    num_lst = [[0 for _ in range(9)] for _ in range(9)]
    for n in range(9):
        num_lst[n] = list(map(int, input().split()))
    result = 1
    for i in range(9):
        num_sum = 0
        for j in range(9):
            num_sum += num_lst[i][j]
        if num_sum != 45:
            result = 0
            break
    print(result, end='')
    if result != 0:
        for j in range(9):
            num_sum = 0
            for i in range(9):
                num_sum += num_lst[i][j]
            if num_sum != 45:
                result = 0
                break
    print(result, end='')
    if result != 0:
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                num_sum = 0
                for i in range(x, x+3):
                    for j in range(y, y+3):
                        num_sum += num_lst[i][j]
                if num_sum != 45:
                    result = 0
                    break
    print(result)
    # print(f'#{t}', result)