arr = [list(map(int, input().split())) for _ in range(3)]
arr_t = list(zip(*arr))
arr_tt = list(map(list, zip(*arr)))
temp = [[0 for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        temp[j][i] = arr[i][j]
        # if i < j:
        #     arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)
print(arr_t)
print(arr_tt)
print(temp)
