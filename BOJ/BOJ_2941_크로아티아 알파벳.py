# Str = input()
# ans = len(Str)
# ans -= (Str.count('c=')*(len('c=')-1))
# ans -= (Str.count('c-')*(len('c-')-1))
# ans -= (Str.count('dz=')*(len('dz=')-1))
# ans -= (Str.count('d-')*(len('d-')-1))
# ans -= (Str.count('lj')*(len('lj')-1))
# ans -= (Str.count('nj')*(len('nj')-1))
# ans -= (Str.count('s=')*(len('s=')-1))
# if 'dz=' in Str:
#     ans -= (Str.count('z=')*(len('z=')-1))-1
# else:
#     ans -= (Str.count('z=') * (len('z=') - 1))
# print(ans)
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b = input()
for i in a:
    b = b.replace(i, 'a')
ans = len(b)
print(ans)