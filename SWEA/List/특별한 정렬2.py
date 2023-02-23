def acsend(arr, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


for t in range(1, int(input())+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    acsend(num_lst, N)
    print(f'#{t}', end=' ')
    for n in range(10):
        if n % 2:
            print(num_lst.pop(0), end=' ')
        else:
            print(num_lst.pop(-1), end=' ')
    print()