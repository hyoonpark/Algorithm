w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

j = (p + t) // w
i = (q + t) // h

if j % 2 == 0:
    x = (p + t) % w
else:
    x = w - (p + t) % w

if i % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h

print(x, y)