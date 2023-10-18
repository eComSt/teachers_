data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
# получаем внутренний список
# print(data[1])
#
# получаем конкретный элемент внутреннего списка
# print(data[0][2])
# summa = 0
# for line in data:
#     for item in line:
#         summa = summa + item
# print(summa)

# summa = 0
# for line in data:
#     summa = summa +sum(line)
# print(summa)

N = int(input('Введите количество учеников:'))
data = []
for i in range(N):
    line = input('Введите ИМЯ БАЛЛ1 БАЛЛ2 БАЛЛ3:').split()
    data.append(line)
