def count_errors(results):
    error_num = 0
    for result in results:
        if result == "ERROR" :
            error_num = error_num+1
    return error_num

if __name__ == "__main__" :
    results = ["PASS", "ERROR", "FAIL", "ERROR", "SKIP"]
    print(f"Error count = {count_errors(results)}")
