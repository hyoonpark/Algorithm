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