def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = arr[(start + end) // 2]  # pivot을 중간값으로 설정

    left, right = start, end
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    quick_sort(arr, start, right)
    quick_sort(arr, left, end)

    return arr


for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = quick_sort(arr, 0, N-1)
    print(f'#{tc}', ans[N//2])