import pytest
from main import checkForDiff


@pytest.mark.parametrize('list1, list2, result', [
    (["first", "second", "third"], ["second", "third", "fourth"], ["first"]),

])
def test_checkForDiff(list1, list2, result):
    check = checkForDiff(list1, list2)
    assert check == result