"""N-th Fibonacci element calculator"""

from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """Caches values of n-th element of Fibonacci sequence 
    that was calculated on previous calls.

    Returns:
        Callable function that calculates n-th element value of Fibonacci sequence.
    """
    cache = dict()
    def fibonacci(n: int) -> int:
        """Returns n-th element value of Fibonacci sequence.
        
        Args:
            n:
                n-th element of Fibonacci sequence.
        
        Returns:
            A value of n-th element of Fibonacci sequence.
        """
        if n < 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

fibonacci = caching_fibonacci()
print(fibonacci(10))
print(fibonacci(15))
