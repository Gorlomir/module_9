def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result <= 1:
            print("Составное")
        elif result == 2:
            print("Простое")
        else:
            if result % 2 == 0:
                print("Составное")
            else:
                for i in range(3, int(result ** 0.5) + 1, 2):
                    if result % i == 0:
                        print("Составное")
                        return
                print("Простое")
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)