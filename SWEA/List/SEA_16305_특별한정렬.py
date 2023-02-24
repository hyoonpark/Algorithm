# 1
def SelectionSort(lst, N):
    for i in range(N-1):
        idx = i
        if i % 2 == 0:
            for j in range(i+1, N):
                if lst[idx] < lst[j]:
                    idx = j
            lst[i], lst[idx] = lst[idx], lst[i]
        else:
            for j in range(i+1, N):
                if lst[idx] > lst[j]:
                    idx = j
            lst[i], lst[idx] = lst[idx], lst[i]
    return lst

T =int(input())
for t in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    SelectionSort(num_lst, N)
    print(f'#{t}', *num_lst[:10])

# 2
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