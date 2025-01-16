def is_prime(func):
    def warpper(*args):
        result = func(*args)
        sum_ = sum(args)
        is_prime = 0
        for i in range(2, int(sum_ ** 0.5) + 1):
            if (sum_ % i == 0):
                is_prime = is_prime + 1
        if is_prime <= 0:
            print("Простое")
        else:
            print("Непростое")
        return result
    return warpper

@is_prime
def sum_three(a, b, c):
    x = (a+b+c)
    return x

result = sum_three(2, 3, 6)
print(result)
