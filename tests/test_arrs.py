import pytest
from utils import arrs


@pytest.mark.parametrize('array, index, default, excepted', [([1, 2, 3], 1, "test", 2),
                                                             ([], 0, "test", "test"),
                                                             ([1, 2], 0, "test", 1)])
def test_get(array, index, default, excepted):
    assert arrs.get(array, index, default) == excepted


@pytest.mark.parametrize('coll, start, end, excepted', [([1, 2, 3, 4], 1, 3, [2, 3]),
                                                        ([1, 2, 3], 1, None, [2, 3]),
                                                        ([], None, None, []),
                                                        ([1, 2, 3, 4, 5], None, None, [1, 2, 3, 4, 5])])
def test_slice(coll, start, end, excepted):
    assert arrs.my_slice(coll, start, end) == excepted
