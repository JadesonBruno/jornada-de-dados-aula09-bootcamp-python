from functools import wraps
from time import time


# Decorador de medida de tempo
def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Tempo de execução: {end - start} segundos")
        return result

    return wrapper
