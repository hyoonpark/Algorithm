def Test(arr):
    for i in range(100):
        for j in range(100-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                return M
    else:
        return 0

def Turn(arr):
    arr_t = list(zip(*arr))
    return arr_t

for _ in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    Turn(arr)
    max_len = 1
    M = 100
    while M > 0:
        if Test(arr) or Test(Turn(arr)):
            max_len = M
            print(f'#{tc}', max_len)
            break
        else:
            M -= 1