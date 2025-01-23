def apply_all_func(int_list, *functions):
    results = {}

    for func in functions:
        try:

            result = func(int_list)
            results[func.__name__] = result
        except TypeError:
            raise ValueError(f"Функция {func.__name__} не принимает список как аргумент")

    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))