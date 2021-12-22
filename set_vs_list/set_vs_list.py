"""
Test: remove duplicates in a sequence.

Compare performance of `set` with `list`
"""
import base64
from collections import namedtuple
from hashlib import sha256
from timeit import timeit

NUMBERS = [(257 + 19*41*n // 37) for n in range(1000)]
STRINGS_1 = [hex(n) for n in range(1000)]  # "0x0" to "0x2709"
STRINGS_2 = [base64.b64encode(sha256(s.encode()).digest()).decode() * 5 for s in STRINGS_1]


def no_duplicates_list(iterable):
    _without_duplicates = []
    for item in iterable:
        if item not in _without_duplicates:
            _without_duplicates.append(item)

    return _without_duplicates


def no_duplicates_set(iterable):
    _unique_keys = set()
    _without_duplicates = []
    for item in iterable:
        if item not in _unique_keys:
            _without_duplicates.append(item)
            _unique_keys.add(item)
    return _without_duplicates


def no_duplicates_set_key(iterable, unique_key=lambda x: x):
    _unique_keys = set()
    _without_duplicates = []
    for item in iterable:
        key_x = unique_key(item)
        if key_x not in _unique_keys:
            _without_duplicates.append(item)
            _unique_keys.add(key_x)
    return _without_duplicates


def no_duplicates_set_key_none(iterable, unique_key=None):
    _unique_keys = set()
    _without_duplicates = []
    for item in iterable:
        key_x = unique_key(item) if unique_key is not None else item
        if key_x not in _unique_keys:
            _without_duplicates.append(item)
            _unique_keys.add(key_x)
    return _without_duplicates


# unique: number of unique elements
# duplicates: number of duplicates, as a slice: array[0:duplicates] or array[-duplicates:]
# repeat: how many times to repeat the duplicates
TEST_CASE = namedtuple("TEST_CASE", "unique,duplicates,repeat")

test_cases = [
    TEST_CASE(1, 0, 0),
    TEST_CASE(1, 1, 1),
    TEST_CASE(1, 1, 10),
    TEST_CASE(1, 1, 100),
    TEST_CASE(5, 0, 0),
    TEST_CASE(5, 1, 1),
    TEST_CASE(5, 1, 10),
    TEST_CASE(5, 5, 10),
    TEST_CASE(10, 0, 0),
    TEST_CASE(10, 1, 10),
    TEST_CASE(10, 10, 1),
    TEST_CASE(10, 10, 10),
    TEST_CASE(100, 0, 0),
    TEST_CASE(100, 10, 10),
    TEST_CASE(100, 10, 100),
    # from this point on, list is far too slow
]

if __name__ == '__main__':
    for test_case in test_cases:
        for name, feed in [("NUMBERS", NUMBERS), ("STRINGS_1", STRINGS_1), ("STRINGS_2", STRINGS_2)]:
            sequence = feed[0:test_case.unique] + (feed[-test_case.duplicates:] * test_case.repeat)
            print(f'--- {test_case}: {name} ---')
            ns = {
                **globals(),
                "iterable": sequence,
            }
            for f in (no_duplicates_list, no_duplicates_set, no_duplicates_set_key, no_duplicates_set_key_none):
                res = timeit(f"{f.__name__}(iterable)", globals=ns, number=10000)
                print(f"{f.__name__}: {res}")
