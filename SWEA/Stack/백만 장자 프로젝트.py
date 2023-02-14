def Benefit(arr):

    cnt = 0
    max_num = arr[N-1]

    for i in range(N-2, -1, -1):
        if arr[i] > max_num:
            max_num = arr[i]
        cnt += (max_num - arr[i])

    return cnt


for t in range(1, int(input())+1):
    N = int(input())  # 예상가능한 일수
    P_lst = list(map(int, input().split()))
    print(f'#{t}', Benefit(P_lst))