# my_set = set()
# my_set_2 = {1,2,3}
# my_set_3 = set([1,2,3])
# my_set_4 = {}

# print(type(my_set))
# print(type(my_set_2))
# print(type(my_set_3))
# print(type(my_set_4))


# This code snippet demonstrates different ways to initialize a set in Python:

# my_set is initialized as an empty set using the set() constructor.
# my_set_2 is initialized with three elements using set literal syntax.
# my_set_3 is initialized with three elements using the set() constructor and a list.
# my_set_4 is initialized as an empty dictionary, not a set.
# my_set = set()
# my_set.add(1)
# my_set.add(2)
# my_set.add(3)
# print(my_set)

#Этот код создает пустое множество с именем my_set. Затем он добавляет числа 1, 2 и 3 в это множество с помощью метода add(). Наконец, он выводит содержимое множества.

# my_set.discard(1)
# print(my_set)
# my_set.discard(2)
# print(my_set)
# my_set.remove(3)
# print(my_set)
# my_set.remove(4)
# print(my_set)
#Этот фрагмент кода демонстрирует использование методов discard() и remove() на объекте множества с именем my_set.

# discard(1) удаляет элемент 1 из множества, если он существует, в противном случае ничего не делает.
# discard(2) удаляет элемент 2 из множества, если он существует, в противном случае ничего не делает.
# remove(3) удаляет элемент 3 из множества, если он существует, в противном случае вызывает KeyError.
# remove(4) удаляет элемент 4 из множества, если он существует, в противном случае вызывает KeyError.


my_set = set()
for i in range(100):
    my_set.add(i)
my_set.clear()
# print(my_set)


my_grades = {3, 4, 5}
your_grades = {2, 4, 5}
sets_intersection = my_grades.intersection_update(your_grades)

# intersection() - пересечение множеств
# print(sets_intersection)
# print(your_grades.intersection(my_grades))
# print(your_grades.union(my_grades))
# print(your_grades.difference(my_grades))
# print(my_grades.difference(your_grades))
# Методы intersection(), union(), difference() не меняют исходные множества, а создают новое множество
# Методы intersection_update(), update(), difference_update() работают также, как их аналоги, но меняют исходное множество
str1 = 'I love cats'
str2 = 'c a t s'
# issubset() - метод, проверяющий являются ли одно множество подмножеством другого
if set(str2).issubset(str1):
    print('Да')
else:
    print('Нет')

n = int(input("Enter Number: "))
result = set()
for i in range(1, n + 1):
    result.add(i)

while True:
    ask = input("Enter Suggestion: ")
    if ask == 'HELP':
        print(result)
        break
    else:
        ask_set = set()
        for elem in ask.split():
            ask_set.add(int(elem))
    answer = input("YES or NO? ")
    if answer == 'YES':
        result.intersection_update(ask_set)
    elif answer == 'NO':
        result.difference_update(ask_set)



