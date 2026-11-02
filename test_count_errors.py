import pytest
from return_practice import count_errors

def test_count_errors():
    statuses = ["PASS", "ERROR", "FAIL", "ERROR", "SKIP"]
    assert count_errors(statuses) == 2

def test_empty_results():
    statuses = []
    assert count_errors(statuses) == 0

# Using parametrize
@pytest.mark.parametrize("data, exp", [
    (["PASS", "ERROR", "FAIL"], 1),
    ([], 0),
    (["ERROR", "ERROR", "ERROR"], 3),
    (["PASS", "FAIL", "SKIP"], 0)
])
def test_multiple_error_scenarios(data, exp):
    assert count_errors(data) == exp
