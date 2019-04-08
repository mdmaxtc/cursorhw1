"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    """
    If @first and @second has the same value should return True
    In another case should return False
    """
    if first == second:
        return True
    else:
        return False


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    """
    If @first and @second has the same type should return True
    In another case should return False
    """
    if type(first) == type(second):
        return True
    else:
        return False


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    """
    If @first and @second are the same object should return True
    In another case should return False
    """
    if first is second:
        return True
    else:
        return False


def multiple_ints(first_value: int, second_value: int) -> int:
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError

    Raises:
        ValueError

    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """
    if type(first_value) != int or type(second_value) != int:
        raise ValueError
    else:
        return first_value * second_value


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise OurAwesomeException

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        OurAwesomeException

    Returns: multiple of two numbers.

    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """
    first_value = int(first_value)
    second_value = int(second_value)
    if type(first_value * second_value) == int:
        return int(first_value) * int(second_value)
    else:
        raise OurAwesomeException


def is_word_in_text(word: str, text: str) -> bool:
    """
    If text contain word return True
    In another case return False.
    
    Args:
        word: Searchable substring
        text: Text for searching

    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False
        
    """
    if word in text:
        return True
    else:
        return False


def some_loop_exercise() -> list:
    """
    Use loop to create list contains int values from 0 to 12 except 6 and 7
    """
    list = []
    i = 0
    while i <= 12:
        list.append(i)
        i += 1
    list.remove(6)
    list.remove(7)
    return list


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
    new_lst = data[:]
    for item in new_lst:
        if item < 0:
            data.remove(item)
    return(data)


def alphabet() -> dict:
    """
    Create dict where keys are alphabetic characters. And values are it number in alphabet
    Notes You could see the implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    dict = {}
    keys = range(1, 26)
    values = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", 
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", 
            "x", "y", "z"]
    for i, k in enumerate(values, 1):
        dict[i] = k
    return(dict)


def simple_sort(data: List[int]) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """
    for i in range(len(data)):
        min = i
        for k in range(i + 1, len(data)):
            if data[k] < data[min]:
                min = k
        data[min], data[i] = data[i], data[min]
    return data
