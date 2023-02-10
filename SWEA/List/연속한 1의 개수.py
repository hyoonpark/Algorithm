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