'''
0. 완전탐색을 할 줄 안다. 완전탐색을 응용해서 문제를 해결할 수 있다.
1. 전체 날짜 수가 100000까지 있으므로 아이디어 싸움이다.
2. 첫번째 경우만 sum 해준다.
3. 그 다음부터 젤 앞요소를 빼주고 K번째를 더해준다.
'''

N, K = map(int, input().split())    # 전체 날짜 수, 연속적인 날짜 수
tem_lst = list(map(int, input().split()))
sum_lst = []
temp = sum(tem_lst[:K])
sum_lst.append(temp)
for x in range(N-K):
    temp -= (tem_lst[x] - tem_lst[x+K])
    sum_lst.append(temp)
ans = max(sum_lst)
print(ans)