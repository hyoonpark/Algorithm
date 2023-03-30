for _ in range(int(input())):
    ans_lst = ['X']+list(input())
    ans = 0
    cnt = 0
    for i in range(1, len(ans_lst)+1):
        if ans_lst[i-1] ==