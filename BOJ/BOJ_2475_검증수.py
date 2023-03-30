lst = map(lambda x: int(x)**2, input().split())
ans = sum(lst)%10
print(ans)