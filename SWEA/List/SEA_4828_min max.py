T = int(input())

for i in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    num_max = max(nums)
    num_min = min(nums)
    sub = num_max - num_min
    print(f'#{i} {sub}')