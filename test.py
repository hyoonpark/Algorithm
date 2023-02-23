a = {'1':2, '2':2}
max_k = max(a, key=a.get)
print(max_k, a.get(max_k))