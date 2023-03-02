'''
0. 2차원 리스트를 만들고, 2차원 리스트를 순회할 수 있다.
1. 빙고판을 2차원 리스트로 받는다.
2. 부르는 숫자들을 리스트로 받아서, 빙고판의 해당 숫자를 0으로 초기화한다.
3. 빙고판의 빙고 줄이 3줄인것이 확인되면 그때의 숫자를 print 한다.
'''

def Check(arr, arr_t):
    cnt = 0    # 빙고 몇줄인지
    rslt = 0    # 좌상에서 아래로 대각선 확인
    rslt_t = 0    # 우상에서 아래로 대각선 확인

    for row in arr:    # 각 행, 열에서 0이 5개면 빙고
        if row.count(0) == 5:
            cnt += 1
    for col in arr_t:
        if col.count(0) == 5:
            cnt += 1

    for i in range(5):    # 대각선 확인
        rslt += arr[i][i]
        if rslt:
            break
    else:
        cnt += 1
    for i in range(5):
        rslt_t += arr[i][4-i]
        if rslt_t:
            break
    else:
        cnt += 1

    if cnt >= 3:
        return True



bingo = [list(map(int, input().split())) for _ in range(5)]

for _ in range(5):
    nums = list(map(int, input().split()))    # 사회자가 부르는 숫자를 5개씩 받아온다.
    for num in nums:
        for i in range(5):
            if num in bingo[i]:    # 빙고판 i행에 그 숫자가 있다면
                j = bingo[i].index(num)
                bingo[i][j] = 0    # 찾아서 0으로 초기화
                bingo_t = list(map(list, zip(*bingo)))    # 그 빙고판을 전치시킨다.
                if Check(bingo, bingo_t):    # 빙고가 3줄인지 확인
                    print(num)
                    exit()    # 빙고 3줄이 될 때 숫자만 print 하면 더 이상 안 돌아도 된다.