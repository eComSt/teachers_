print({int(i):sum(map(int,i)) for i in input().split()})
print({int(i):sum([int(j) for j in i]) for i in input().split()})