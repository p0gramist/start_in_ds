import time
from functools import wraps, lru_cache


def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения функции {func.__name__}: {end - start}")
        return result
    return wrapper


def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Функция вызвана с параметрами:\n{args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper


def counter(func):
    counters = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if func.__name__ in counters:
            counters[func.__name__] += 1
        else:
            counters[func.__name__] = 1
        result = func(*args, **kwargs)

        number_of_count = str(counters[func.__name__])
        print(f"Функция была вызвана: {number_of_count} раз{'а' if number_of_count[-1] in ['2', '3', '4'] else ''}")

        return result

    return wrapper


def memo(func):
    # Вариант с декоратором lru_cache - слишком "пустой", чтобы использовать так
    #     (логичнее ставить напрямую на декорируемую функцию)
    """
    @lru_cache
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    """

    cache = {}  # используется механизм замыкания для кеширования результатов

    @wraps(func)
    def wrapper(*args, **kwargs):
        if f"{func.__name__}_{args}_{kwargs}" in cache:
            print(f"Результат функции {func.__name__} был взят из кэша")
            return cache[f"{func.__name__}_{args}_{kwargs}"]
        else:
            result = func(*args, **kwargs)
            cache[f"{func.__name__}_{args}_{kwargs}"] = result
            print(f"Результат функции {func.__name__} был записан в кэш")
            return result
    return wrapper