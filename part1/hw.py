from random import randint
N, M = int(input()), int(input())
n_gen = [randint(1, 100) for _ in range(N)]
m_gen = [randint(1, 100) for _ in range(M)]
n_set = set(n_gen)
m_set = set(m_gen)
print(len(n_set.intersection(m_set)))