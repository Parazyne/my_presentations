from add import add_two_numbers
import pytest


@pytest.fixture(scope='function')
def numbers_data(request):
    print('\nSetup')

    def fin():
        print('\nTeardown')
    request.addfinalizer(fin)

    return 1, 2, 3


def test_add(numbers_data):
    n1, n2, expected_value = numbers_data
    print('Test func #1')
    assert add_two_numbers(n1, n2) == expected_value


def test_another(numbers_data):
    n1, n2, expected_value = numbers_data
    print('\nTest Func #2')
    assert add_two_numbers(n1, n2) == expected_value
