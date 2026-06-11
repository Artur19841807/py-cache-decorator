from typing import Callable

def cache(func):
    results_cache = {}

    def inner(*args, **kwargs):
        cache_key = (args, tuple(kwargs.items()))
        
        if cache_key not in results_cache:
            print("Calculating new result")
            results_cache[cache_key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
            
        return results_cache[cache_key]

    return inner
