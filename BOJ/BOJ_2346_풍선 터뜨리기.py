import sys
from collections import deque

N = int(sys.stdin.readline())
nums = deque(i for i in range(1, N+1))
arr = deque(map(int, input().split()))
x = nums.popleft()
print(x, end=' ')
while nums:
    if arr[x-1] > 0:
        nums.rotate(-(arr[x-1])+1)
    else:
        nums.rotate(-(arr[x-1]))
    x = nums.popleft()
    print(x, end=' ')