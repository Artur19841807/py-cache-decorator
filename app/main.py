from typing import Callable

def cache(func: Callable) -> Callable:
    results_cache = {}

    def inner(*args, **kwargs):
        cache_key = (args, tuple(kwargs.items()))
        
        if cache_key not in results_cache:
            results_cache[cache_key] = func(*args, **kwargs)
            
        return results_cache[cache_key]

    return inner
