T = int(input())

for i in range(1, T+1):
    N = int(input())
    nums = int(input())
    counts = [0] * 11
    cnt = 0
    for _ in range(len(str(nums))):
        counts[nums % 10] += 1
        nums = nums // 10
    for j in range(10):
        if counts[j] >= cnt:
            num_max = j
            cnt = counts[j]


    print(f'#{i} {num_max} {max(counts)}')
    # print(f'#{i}', num_max, max(counts))
