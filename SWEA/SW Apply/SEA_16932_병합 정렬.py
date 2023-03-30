def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    return merge(left_arr, right_arr)


def merge(left, right):
    global cnt
    merged = []
    left_index = right_index = 0
    # if left[-1] > right[-1]:
    #     cnt += 1

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    if left_index < len(left):
        merged.extend(left[left_index:])
        cnt += 1


    if right_index < len(right):
        merged.extend(right[right_index:])

    return merged


for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    lst = merge_sort(arr)
    print(f'#{tc}', lst[N//2], cnt)