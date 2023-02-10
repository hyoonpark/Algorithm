T = int(input())

for t in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    num_lst.sort()
    print(f'#{t}', *num_lst)