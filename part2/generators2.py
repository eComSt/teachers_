# numbers = [i**2 for i in range(1, int(input("Введите N: ")) + 1)]
# print(numbers)
# symbols = [sym for sym in input("Введите строку: ")]
# symbols = list(input("Введите строку: "))
# number = []
# for i in range(1, 1001):
#     if i%7 == 0:
#         number.append(i)
numbers = [i for i in range(100, 1001) if i%7 == 0]
print(numbers)