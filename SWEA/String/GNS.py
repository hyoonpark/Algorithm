a_nums = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
for _ in range(1, int(input())+1):
    t, lth = input().split()
    num_lst = list(input().split())
    for i in range(int(lth) - 1):
        for j in range(i, int(lth)):
            if a_nums[num_lst[i]] > a_nums[num_lst[j]]:
                num_lst[i], num_lst[j] = num_lst[j], num_lst[i]
    word = ' '.join(num_lst)
    print(word)
