# 1
T = int(input())
for t in range(1, T+1):
    N = int(input())
    mylist = [[0 for _ in range(10)] for _ in range(10)]
    for _ in range(N):
        a_lst = list(map(int, input().split()))
        for i in range(a_lst[0], a_lst[2]+1):
            for j in range(a_lst[1], a_lst[3]+1):
                mylist[i][j] += a_lst[-1]
    cnt = 0
    for k in mylist:
        cnt += k.count(3)
    print(f'#{t} {cnt}')

# 2
T = int(input())
for t in range(1, T+1):
    N = int(input())
    mylist = [[0 for _ in range(10)] for _ in range(10)]
    cnt = 0
    for _ in range(N):
        a_lst = list(map(int, input().split()))
        for i in range(a_lst[0], a_lst[2]+1):
            for j in range(a_lst[1], a_lst[3]+1):
                if a_lst[-1] == 1 and (mylist[i][j] == 0 or mylist[i][j] == 2):
                    cnt += a_lst[-1]
                elif a_lst[-1] == 2 and (mylist[i][j] == 0 or mylist[i][j] == 1):
                    cnt += a_lst[-1]
    print(cnt)