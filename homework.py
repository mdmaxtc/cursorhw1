"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    if first == second:
        return True
    else:
        return False


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    if type(first) == type(second):
        return True
    else:
        return False


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    if first is second:
        return True
    else:
        return False


def multiple_ints(first_value: int, second_value: int) -> int:
    if type(first_value) != int or type(second_value) != int:
        raise ValueError
    else:
        return first_value * second_value


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    first_value = int(first_value)
    second_value = int(second_value)
    if type(first_value * second_value) == int:
        return int(first_value) * int(second_value)
    else:
        raise OurAwesomeException


def is_word_in_text(word: str, text: str) -> bool:
    if word in text:
        return True
    else:
        return False


def some_loop_exercise() -> list:
    list = []
    i = 0
    while i <= 12:
        list.append(i)
        i += 1
    list.remove(6)
    list.remove(7)
    return list


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    new_lst = data[:]
    for item in new_lst:
        if item < 0:
            data.remove(item)
    return(data)


def alphabet() -> dict:
    dict = {}
    keys = range(1, 26)
    values = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", 
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", 
            "x", "y", "z"]
    for i, k in enumerate(values, 1):
        dict[i] = k
    return(dict)


def simple_sort(data: List[int]) -> List[list]:
    for i in range(len(data)):
        min = i
        for k in range(i + 1, len(data)):
            if data[k] < data[min]:
                min = k
        data[min], data[i] = data[i], data[min]
    return data
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """
