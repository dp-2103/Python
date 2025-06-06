# 1. Numeric Types
a = 10               # int
b = 3.14             # float
c = 2 + 3j           # complex

print(a, type(a))    # 10 <class 'int'>
print(b, type(b))    # 3.14 <class 'float'>
print(c, type(c))    # (2+3j) <class 'complex'>


# 2. Sequence Types
my_list = [1, 2, 3]          # list (mutable)
my_tuple = (4, 5, 6)         # tuple (immutable)
my_range = range(0, 5)       # range (immutable sequence)

print(my_list, type(my_list))    # [1, 2, 3] <class 'list'>
print(my_tuple, type(my_tuple))  # (4, 5, 6) <class 'tuple'>
print(list(my_range), type(my_range))  # [0, 1, 2, 3, 4] <class 'range'>


# 3. Text Type
my_str = "Hello, Python!"        # string

print(my_str, type(my_str))      # Hello, Python! <class 'str'>


# 4. Set Types
my_set = {1, 2, 3}               # set (unordered, unique)
my_frozenset = frozenset([4, 5, 6])  # frozenset (immutable set)

print(my_set, type(my_set))          # {1, 2, 3} <class 'set'>
print(my_frozenset, type(my_frozenset))  # frozenset({4, 5, 6}) <class 'frozenset'>


# 5. Mapping Type
my_dict = {'name': 'Alice', 'age': 25}   # dictionary (key-value pairs)

print(my_dict, type(my_dict))         # {'name': 'Alice', 'age': 25} <class 'dict'>


# 6. Boolean Type
is_active = True
is_done = False

print(is_active, type(is_active))     # True <class 'bool'>
print(is_done, type(is_done))         # False <class 'bool'>


# 7. Binary Types
my_bytes = b'hello'                  # bytes (immutable)
my_bytearray = bytearray(b'world')  # bytearray (mutable)

print(my_bytes, type(my_bytes))         # b'hello' <class 'bytes'>
print(my_bytearray, type(my_bytearray)) # bytearray(b'world') <class 'bytearray'>
