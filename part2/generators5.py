def get_d(n):
    divisors = []
    for i in range(2, n//2 + 1):
        if n%i == 0:
            divisors.append(i)
    return divisors
N =5
M=20
num_divs = {num:get_d(num) for num in range(N, M+1) if len(get_d(num))>0}
print(num_divs)