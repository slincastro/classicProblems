from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}

def fib_in_memmory (n: int) -> int:
    if n not in memo:
        memo[n] = fib_in_memmory(n - 1) + fib_in_memmory(n - 2)
    return memo[n]


def fib_recursive(n: int) -> int:
    if n == 0 : return n
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last + next

    return next


print(fib_in_memmory(10))
print(fib_recursive(10))
