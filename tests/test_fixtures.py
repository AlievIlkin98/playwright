import pytest

@pytest.mark.parametrize('num_one, num_2, result',[
    (1,2,3),
    (2,4,9)
])
def test_is_equal(num_one, num_2, result):
    assert  num_one + num_2 == result, 'Failed'
