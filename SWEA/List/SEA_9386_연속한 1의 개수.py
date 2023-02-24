# 1
T = int(input())

for t in range(1, T+1):
    N = int(input())
    nums = input()
    cnts = 0
    cnts_list = []
    for i in nums:
        if i == '1':
            cnts += 1
            cnts_list.append(cnts)
        else:
            cnts_list.append(cnts)
            cnts = 0
    print(f'#{t}', max(cnts_list))

# 2
for t in range(1, int(input())+1):
    N = int(input())
    a_lst = list(input())
    cnt = 0
    max_cnt = 0
    for i in range(N):
        if a_lst[i] == '1':
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
            cnt = 0
        if i == N-1:
            if cnt > max_cnt:
                max_cnt = cnt
    print(f'#{t}', max_cnt)