numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
b = 1
a = len(numbers)
c = 0
while b <= a:
    if b != a:
        c = numbers[b]
        b = b+1
        is_prime = 0
        for i in range(2, int(c ** 0.5) + 1):
            if (c % i == 0):
                is_prime = is_prime + 1
        if is_prime <= 0:
            primes.append(b)
        else:
            not_primes.append(b)
    else:
        break
print("Простые",primes)
print("Не простые",not_primes)
