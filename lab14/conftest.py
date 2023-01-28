import pytest


@pytest.fixture
def check_palindrome_fixture():
    print('\nStart of check palindrome fixture')
    yield 'khokho'
    print('\End of check palindrome fixture')
    