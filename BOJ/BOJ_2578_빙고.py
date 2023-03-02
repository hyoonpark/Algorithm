def check(arr, arr_t):
    cnt = 0  # 빙고 몇줄인지
    rslt = 0  # 좌상에서 아래로 대각선 확인
    rslt_t = 0  # 우상에서 아래로 대각선 확인

    for row in arr:  # 각 행, 열에서 0이 5개면 빙고
        if row.count(0) == 5:
            cnt += 1
    for col in arr_t:
        if col.count(0) == 5:
            cnt += 1

    for i in range(5):  # 대각선 확인
        rslt += arr[i][i]
        if rslt:
            break
    else:
        cnt += 1
    for i in range(5):
        rslt_t += arr[i][4 - i]
        if rslt_t:
            break
    else:
        cnt += 1
    if cnt >= 3:
        return True


bingo = [list(map(int, input().split())) for _ in range(5)]
flag = True
for x in range(5):
    if flag:
        nums = list(map(int, input().split()))
        for num in nums:
            if flag:
                for i in range(5):
                    if num in bingo[i]:
                        j = bingo[i].index(num)
                        bingo[i][j] = 0
                        bingo_t = list(map(list, zip(*bingo)))
                        if check(bingo, bingo_t):
                            print(x*5+(nums.index(num)+1))
                            flag = False