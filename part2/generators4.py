from pprint import pprint
square = {}
for i in range(1, 21):
    square[i] = i**0.5
square = {i:i**0.5 for i in range(1, 21) if i%2 == 0}

# pprint(square)
fruits = {
    'яблоко': 100,
    'груша': 200,
    'апельсин': 300
}
fruits = {
    'яблоко': 100,
    'груша': 200,
    'апельсин': 300,
    'банан': 400
}
fruits_new = {i:j*1.2 for i, j in fruits.items()}
# pprint(fruits_new)
N=5
table = []
for i in range(1,N+1):
    row = []
    for j in range(1,N+1):
        row.append(i*j)
    table.append(row)
N=5
table = [[i*j for j in range(1,N+1)]for i in range(1,N+1)]
pprint(table)