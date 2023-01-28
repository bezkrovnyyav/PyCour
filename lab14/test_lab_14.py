'''
Testing¶
In this task you need to cover with tests all tasks from the lab1.

Testing¶
In this task you need to cover with tests all tasks from the lab1.

Use pytest.

Create fixtures, use parametrize, mocks and marks.

Note: try to cover the code with no less than 5 tests each task

pytest -v -s test_lab_14.py
coverage run -m pytest test_lab_14.py
coverage report -m
'''
import pytest

from task_1 import check_palindrome
from task_2 import multiply_num
from task_3 import check_balanced


@pytest.mark.parametrize("input_data, expected_result", [
    ("", ('Palindrome', 'Symmetrical')),
    ("khokho", ('Not palindrome', 'Symmetrical')),
    ("abc", ('Not palindrome', 'Not symmetrical')),
    ("Do geese see God?", ('Not palindrome', 'Not symmetrical')),
    ("amaama", ('Palindrome', 'Symmetrical')),
    ])
def test_diff_input_palindrome_and_symmetrical(input_data, expected_result):
    assert check_palindrome(input_data) == expected_result, "Error not symmetrical and palindrome"


def test_palindrome(check_palindrome_fixture):
    assert check_palindrome(check_palindrome_fixture) == (
        "Not palindrome", "Symmetrical"
    ), "Error in entered string"


@pytest.mark.parametrize("first_num, second_num, expected_result", [
    (-1, 5, -5),
    (4, 6, 24),
    (3.6, 10, 36),
    (1.0, 8.0, 8),
    (30, 30, 900),
    ])
def test_check_multiply_num(first_num, second_num, expected_result, mocker):
    mocker.patch('task_2.time.sleep', return_value=None)
    assert multiply_num(first_num, second_num) == expected_result, \
        "Error at multiply_without_multiply()"


@pytest.mark.parametrize("input_data, expected_result", [
    ('{][{()}}', 'Unbalanced'),
    ('{][{(%)}}', 'Unbalanced'),
    ('{[]{()}}', 'Balanced'),
    ('[{}{}(]', 'Unbalanced'),
    ('{][{()}}$$', 'Unbalanced'),
    ('{', 'Unbalanced'),
    ])
def test_check_balanced(input_data, expected_result):
    assert check_balanced(input_data) == expected_result, "Value should be mocked"
