"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List

# alphabet = {}
# value = 0
# for letter in range(97,123):
#     value
#     alphabet[chr(letter)]
def simple_sort(data: List[int]) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:
    """
#     for i in range(0, len(data)):
#         for j in range(1, len(data) - i):
#             if data[j - 1] > data[j]:
#                 data[j - 1], data[j] = data[j], data[j - 1]
#
#     return data
# print(simple_sort([2, 9, 6, 7, 3, 2, 1]))

data = [2, 9, 6, 7, 3, 2, 1]

for value in range(len(data)):
    for simile in range(len(data)):
        print(data[value] < data[simile])
        if data[value] < data[simile]:
            data[value],data[simile] = data[simile],data[value]
    # break
print(data)