T = int(input())

for tc in range(T):
    matrix = []
    for i in range(9):
        matrix.append(list(map(int, input().split())))
#가로순회
    for i in range(9):
        test = []
        for j in range(9):
            test.append(matrix[i][j])
        if len(set(test)) == 9:
            ans = 1
        else:
            ans = 0
            break

    #세로순회
    for j in range(9):
        test1 = []
        for i in range(9):
            test1.append(matrix[i][j])
        if len(set(test1)) == 9:
            ans1 = 1
        else:
            ans1 = 0
            break
    #
    # print(ans, end='')
    # print(ans1, end='')
    #3*3순회
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            test2 = []
            for k in range(3):
                for l in range(3):
                    test2.append(matrix[i+k][j+l])
            if len(set(test2)) == 9:
                ans2 = 1
            else:
                ans2 = 0
                break
    print(ans, ans1, ans2)
    # if ans == 1 and ans1 ==1 and ans2 == 1:
    #     print(1)
    # else:
    #     print(0)