from return_practice import count_errors

def test_count_errors():
    statuses = ["PASS", "ERROR", "FAIL", "ERROR", "SKIP"]
    assert count_errors(statuses) == 2

def test_empty_results():
    statuses = []
    assert count_errors(statuses) == 0
