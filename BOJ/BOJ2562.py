num_lst = []
for _ in range(9):
    num_lst.append(int(input()))
M = max(num_lst)
print(M)
print(num_lst.index(M)+1)