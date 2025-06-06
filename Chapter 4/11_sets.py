#set does not includes repeated values
e = set()   #empty set

s = {1, 5, 9, 5, 5, 5}
print(s)
print(type(s))

#properties of set
'''Unordered — Elements have no defined order; you can’t access by index.

Unique elements — No duplicates allowed; all elements are distinct.

Mutable — You can add or remove elements after creation.

Unindexed — You cannot access elements by position (no indexing or slicing).

Heterogeneous — Can store elements of different data types (ints, strings, tuples, etc.).

Iterable — You can loop through all elements in a set.

No mutable elements — Elements themselves must be immutable (e.g., you can’t put a list inside a set, but you can put a tuple).'''