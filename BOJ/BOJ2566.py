nums = [list(map(int, input().split())) for _ in range(9)]
nums_t = list(zip(*nums))
mx = 0
row, col = 0, 0
for i in range(9):
    for j in range(9):
        if nums[i][j] >= mx:
            mx = nums[i][j]
            row, col = i+1, j+1
        if nums_t[i][j] > mx:
            mx = nums_t[i][j]
            row, col = j+1, i+1

print(mx)
print(row, col)