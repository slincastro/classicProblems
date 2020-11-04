from typing import Dict
from typing import Generator

memo: Dict[int, int] = {0: 0, 1: 1}

def fib_in_memory (n: int) -> int:
    if n not in memo:
        memo[n] = fib_in_memory(n - 1) + fib_in_memory(n - 2)
    return memo[n]


def fib_recursive(n: int) -> int:
    if n == 0 : return n
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last + next #review the tuple unpacking here

    return next

def fib_generation(n: int) -> Generator[int, None, None] :
    yield 0
    if n > 0 : yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next


print(fib_in_memory(10))
print(fib_recursive(10))

for i in fib_generation(10):
    print(i)
