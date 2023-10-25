my_tuple = (1, 2, 3)
my_tuple_1 = tuple([1,2,3])
# print(type(my_tuple))
# print(type(my_tuple_1))
#Этот код создает два кортежа, my_tuple и my_tuple_1, содержащих одни и те же элементы. Первый кортеж создается с использованием круглых скобок, а второй кортеж создается с использованием функции tuple(). Вызовы print() отображают тип каждого кортежа.

# print(my_tuple[1])
# my_tuple[1] = 4

combine_tuple = ([1,2,3],[4,5,6])
# print(combine_tuple)
combine_tuple[0][2] = 7
# print(combine_tuple)

#Строка print(my_tuple[1]) выводит второй элемент кортежа my_tuple.

# Строка my_tuple[1] = 4 пытается присвоить новое значение (4) второму элементу кортежа my_tuple. Однако, кортежи являются неизменяемыми (immutable) в Python, поэтому эта строка вызовет ошибку.

# Строка combine_tuple = ([1,2,3],[4,5,6]) создает кортеж combine_tuple, который содержит два списка в качестве элементов.

# Строка combine_tuple[0][2] = 7 изменяет третий элемент первого списка внутри кортежа combine_tuple на значение 7. Получившийся кортеж будет ([1,2,7],[4,5,6]).

combine_tuple_1 = (1,2,3,4,5,6)
# print(combine_tuple_1[1:4])

object_tuple = (1,2,3)
first,second,third = object_tuple
#Этот код создает кортеж с тремя элементами: 1, 2 и 3, и затем распаковывает кортеж в три переменные: first, second и third, присваивая каждый элемент кортежа соответствующей переменной.
# print(first)
# print(second)
# print(third)


# for i in object_tuple:
#     print(i)
# print(dir(tuple))

# У кортежей есть 2 метода - сount() и index() - работают также, как и со списками
objects_tuple = (1, 2, 3, 1)
# print(objects_tuple.count(2))
# print(objects_tuple.index(1))

# Сложение кортежей (через оператор +)
first_tuple = (1, 2)
second_tuple = (3, 4)
third_tuple = first_tuple + second_tuple
sliced_tuple = first_tuple[1:] + second_tuple[1:]
# создаем новый кортеж и кладем на место старого
first_tuple = first_tuple + second_tuple
# print(first_tuple)
# print(sliced_tuple)
# print(third_tuple)



# Функции и кортежи
# Когда функция возвращает несколько значений через запятую - генерируется и возвращается кортеж
# def func(a, b, c):
#     summa = a + b + c
#     diff = a - b - c
#     return summa, diff

# objects_tuple = (1, 2, 3)
# result = func(*objects_tuple)
# print(result)
# summa, difference = func(*objects_tuple)
# print(summa, difference)


empty_tuple = (1,)
print(empty_tuple)
print(type(empty_tuple))

# проверка, является ли кортеж пустым или нет
# if empty_tuple:
#     print('Кортеж не пустой')
# else:
#     print('Кортеж пустой')


# если внутри кортежа хранятся изменяемые объекты, то их можно менять
tuple_with_lists = ([1, 2, 3], [4, 5, 6])
tuple_with_lists[0].append(4)
# print(tuple_with_lists)

import sys
print("LIST")
object_list = []
print(sys.getsizeof(object_list))
object_list = [1]
print(sys.getsizeof(object_list))
object_list = [1,2]
print(sys.getsizeof(object_list))
object_list = []
for i in range(100_000_000):
    object_list.append(i)
print(sys.getsizeof(object_list))
print('_'*15)
print("TUPLE")
object_list = tuple()
print(sys.getsizeof(object_list))
object_list = tuple([1,])
print(sys.getsizeof(object_list))
object_list = tuple([1,2])
print(sys.getsizeof(object_list))
object_list = []
object_list = (i for i in range(100_000_000))
# object_list = tuple(object_list)    
print(sys.getsizeof(object_list))


a = (1,2)
b,c  = a
b = a[0]
c = a[1]