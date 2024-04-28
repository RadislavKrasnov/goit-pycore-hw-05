"""Sum profit calculator from text"""

from typing import Callable, Generator
import re

def generator_numbers(text: str) -> Generator[float, None, None]:
    """Returns generator.

    Args:
        text:
            string that contains numbers to parse and sum up.
    
    Returns:
        Generator that yields flaot numbers.
    """
    numbers = [float(chunk) for chunk in text.split() if chunk.replace(".", "").isnumeric()]
    for number in numbers:
        yield number

def sum_profit(text: str, func: Callable[[str], int]) -> float|int:
    """Returns sum of profit numbers from text.

    Args:
        text:
            string that contains profit numbers.
        func:
            Callback function that should parse numbers and return them as a Generator.

    Returns:
        Sum of all profit numbers from the text string
    """
    sum_profit = 0
    for num in func(text):
        sum_profit += num
    return sum_profit

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
