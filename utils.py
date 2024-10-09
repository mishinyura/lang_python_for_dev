import time
from typing import Callable, Any

def timer(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start = time.time()
        print('Работа', func.__name__, 'началась')
        result = func(*args, **kwargs)
        print('Работа завершена:', time.time() - start)
        return result
    return wrapper