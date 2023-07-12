m = int(input())
n = int(input())
k = int(input())

rs = [['B']* m] * n
print(type(rs))
print(rs) # [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]
for i in range(k):
    a, b = input().split()
    b = int(b) - 1
    if a == 'R':
        u = len(rs[b])
        for o in range(u):
            print(rs)
            print(rs[b][o])
            rs[b][o] = 'G'


    else:
        for j in range(len(rs)):
            rs[j][b] = 'G'

print(rs)