def analyze_results(results):
    pass_num = 0
    fail_num = 0
    skip_num = 0
    error_num = 0
    for result in results:
        if result == "PASS":
            pass_num = pass_num + 1
        elif result == "FAIL":
            fail_num = fail_num + 1
        elif result == "SKIP":
            skip_num = skip_num + 1
        elif result == "ERROR":
            error_num = error_num + 1
    print(f"Total Tests: {len(results)}")
    print(f"Passed: {pass_num}")
    print(f"Failed: {fail_num}")
    print(f"Skipped: {skip_num}")
    print(f"Errored: {error_num}")

if __name__ == "__main__" :
    results = ["PASS", "FAIL", "SKIP", "PASS", "FAIL", "SKIP", "ERROR"]
    analyze_results(results)
