from collections import deque

N = int(input())
if N == 1:
    cards = deque([1])
elif N % 2:
    cards = deque(i for i in range(4, N+1, 2)) + deque([2])
else:
    cards = deque(i for i in range(2, N+1, 2))
while len(cards) > 1:
    cards.popleft()
    cards.rotate(-1)
print(*cards)