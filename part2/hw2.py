# def Intresting(word):
#     return len(set(word))==len(word)
# data = input().split()
# filtered_data = list(filter(Intresting, data))


filtered_data = list(filter(lambda x: len(set(x))==len(x), input().split()))
print(len(filtered_data))

