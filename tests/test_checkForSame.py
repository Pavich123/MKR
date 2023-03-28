import pytest
from main import checkForSame


@pytest.mark.parametrize('list1, list2, result', [
    (["first", "second", "third"], ["second", "third", "fourth"], ["second", "third"]),

])
def test_checkForSame(list1, list2, result):
    check = checkForSame(list1, list2)
    assert check == result