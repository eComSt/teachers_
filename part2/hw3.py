# with open('data.txt', 'r') as f:
#     summ, choko = 0, 0
#     for line in f:
#         try: summ = summ + int(line)
#         except: choko = choko + 1
f = open('data.txt', 'r')
summ, choko = 0, 0
for line in f:
    try: summ = summ + int(line)
    except: choko = choko + 1
f.close()
print(summ,choko)