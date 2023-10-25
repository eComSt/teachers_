c = (1, 2, 3, 4, 5, 6, 7, 8, 9)
n = int(input())
l = []
for i in c:
    if i!=n:
        l.append(i)
l = tuple(l)
print(l)