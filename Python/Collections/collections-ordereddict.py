#!/usr/bin/env python3

# collections.OrderedDict

# An OrderedDict is a dictionary that remembers the order of the keys
# that were inserted first. If a new entry overwrites an existing entry,
# the original insertion position is left unchanged.

# Example

# Code

# >>> from collections import OrderedDict
# >>>
# >>> ordinary_dictionary = {}
# >>> ordinary_dictionary['a'] = 1
# >>> ordinary_dictionary['b'] = 2
# >>> ordinary_dictionary['c'] = 3
# >>> ordinary_dictionary['d'] = 4
# >>> ordinary_dictionary['e'] = 5
# >>>
# >>> print ordinary_dictionary
# {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
# >>>
# >>> ordered_dictionary = OrderedDict()
# >>> ordered_dictionary['a'] = 1
# >>> ordered_dictionary['b'] = 2
# >>> ordered_dictionary['c'] = 3
# >>> ordered_dictionary['d'] = 4
# >>> ordered_dictionary['e'] = 5
# >>>
# >>> print ordered_dictionary
# OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

# Input Format

# The first line contains the number of items, N.
# The next N lines contains the item's name and price, separated by a space.

# Output Format

# Print the item_name and net_price in order of its first occurrence.

from collections import OrderedDict

supermarket = OrderedDict()

for _ in range(int(input())):
    item = input().rpartition(' ')
    supermarket[item[0]] = supermarket[item[0]] + int(item[-1]) if \
        item[0] in supermarket else int(item[-1])

for item_name in supermarket:
    print(item_name, supermarket[item_name])
