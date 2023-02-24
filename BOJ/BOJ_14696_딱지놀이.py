N = int(input())
for _ in range(N):
    A = {'1':0, '2':0, '3':0, '4':0}
    B = {'1':0, '2':0, '3':0, '4':0}
    a, *nums = input().split()
    b, *ints = input().split()
    for n in nums:
        A[n] += 1
    for m in ints:
        B[m] += 1
    if A['4'] == B['4']:
        if A['3'] == B['3']:
            if A['2'] == B['2']:
                if A['1'] == B['1']:
                    ans = 'D'
                elif A['1'] > B['1']:
                    ans = 'A'
                else:
                    ans = 'B'
            elif A['2'] > B['2']:
                ans = 'A'
            else:
                ans = 'B'
        elif A['3'] > B['3']:
            ans = 'A'
        else:
            ans = 'B'
    elif A['4'] > B['4']:
        ans = 'A'
    else:
        ans = 'B'
    print(ans)