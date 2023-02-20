num_lst = [0] * (10**6+1)
for i in range(len(num_lst)):
    num_lst[i] = i ** 3

for tc in range(1, int(input())+1):
    N = int(input())
    if N in num_lst:
        ans = num_lst.index(N)
    else:
        ans = -1

    print(f'#{tc}', ans)