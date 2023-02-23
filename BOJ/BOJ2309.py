# 방법1
N = 9
temp1 = 0
temp2 = 0
h_lst = [int(input()) for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        if sum(h_lst) - (h_lst[i] + h_lst[j]) == 100:
            temp1 = h_lst[i]
            temp2 = h_lst[j]
            break

h_lst.remove(temp1)
h_lst.remove(temp2)
h_lst.sort()

for h in h_lst:
    print(h)

# 방법2
N = 9
temp1 = 0
temp2 = 0
h_lst = [int(input()) for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        if sum(h_lst) - (h_lst[i] + h_lst[j]) == 100:
            h_lst.remove(h_lst[i])
            h_lst.remove(h_lst[j])
            h_lst.sort()
            for h in h_lst:
                print(h)
            exit()