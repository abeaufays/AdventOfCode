import pytest
from y24.d16 import part2


@pytest.mark.skip()
def test_answer():
    assert part2.answer("y24/d16/test1") == 45
    assert part2.answer("y24/d16/test2") == 64
