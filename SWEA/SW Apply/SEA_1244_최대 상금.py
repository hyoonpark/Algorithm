def dfs(arr, count, max_count):
    global max_val

    if count == max_count:
        num = int(''.join(map(str, arr)))
        max_val = max(max_val, num)
        return

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            if tuple(arr) not in visited[count+1]:
                visited[count + 1].add(tuple(arr))
                dfs(arr, count + 1, max_count)
            arr[i], arr[j] = arr[j], arr[i]


for tc in range(1, int(input())+1):
    arr, cnt = input().split()
    arr = list(map(int, arr))
    cnt = int(cnt)
    max_val = 0
    visited = [set() for _ in range(cnt + 1)]
    dfs(arr, 0, cnt)
    # print(visited)
    print(f'#{tc}', max_val)
