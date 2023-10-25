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

# N = int(input('Введите количество учеников:'))
# data = []
# for i in range(N):
#     line = input('Введите ИМЯ БАЛЛ1 БАЛЛ2 БАЛЛ3:').split()
#     data.append(line)

# subject_1 = 0
# subject_2 = 0
# subject_3 = 0

# for line in data:
#     summa = int(line[1]) + int(line[2]) + int(line[3])
#     print(f'Сумма баллов ученика {line[0]}: {summa}')
#     subject_1 += int(line[1])
#     subject_2 += int(line[2])
#     subject_3 += int(line[3])

# print(f'Средний балл по Предмету1: {subject_1/N}')
# print(f'Средний балл по Предмету2: {subject_2/N}')
# print(f'Средний балл по Предмету3: {subject_3/N}')

# Вложенные словари

# Задача про учеников и ЕГЭ (усложненная)

data = {
    'Петя': {'Физика': 50, 'Математика': 80, 'Биология': 90},
    'Ваня': {'Математика': 65, 'Химия': 64, 'Физика': 90, 'РЯ': 78},
    'Катя': {'РЯ': 45, 'История': 57, 'Математика': 87}
}

for name, subjects in data.items():
    print(f'Сумма баллов ученика {name}:{sum(subjects.values())}')

subject_scores = {}
for line in data.values():
    for subject in line.keys():
        if subject in subject_scores:
            subject_scores[subject].append(line[subject])
        else:
            subject_scores[subject] = [line[subject]]
from pprint import pprint
for subject, scores in subject_scores.items():
    print(f'Средний балл по предмету {subject}:{sum(scores) / len(scores)}')

pprint(subject_scores)