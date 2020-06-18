from add import add_two_numbers
import pytest


@pytest.fixture(params=["1, 3", "2, 5"])
def numbers_data(request):
    # Setup code
    print('\nSetup')
    n1 = request.param[0]
    n2 = request.param[1]
    expected = n1 + n2

    def fin():
        # teardown code
        print('\nTeardown')
    request.addfinalizer(fin)

    return n1, n2, expected


def test_add(numbers_data):
    n1, n2, expected_value = numbers_data
    print('Test func')
    assert add_two_numbers(n1, n2) == expected_value
