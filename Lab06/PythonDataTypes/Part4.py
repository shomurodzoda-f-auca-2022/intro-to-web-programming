unique_numbers = {1, 2, 3, 3, 4, 5, 5, 4}    # Set data structure
print(unique_numbers, type(unique_numbers))

frozen_set = frozenset(unique_numbers)       # FrozenSet, just like set, but immutable
print(frozen_set, type(frozen_set))