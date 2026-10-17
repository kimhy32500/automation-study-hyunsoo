import json
import os

test_log = "test_log.txt"
json_name = "summry.json"

def load_log_file():
    if not os.path.exists(test_log):
        print(f"'{test_log}'파일 없음.")
        return[]

    try:
        with open(test_log, "r", encoding="utf-8") as f:
            log_lines = f.readlines()
        print(f"{len(log_lines)}줄의 로그 확인")
        return log_lines
    except Exception as e:
        print(f"로그 불러오는중 오류 발생 - {e}")
        return []

def parse_log():
    log_line = load_log_file()
    if not log_line:
        return

    total_test = 0
    total_pass = 0
    total_fail = 0
    fail_test = []

    for line_num, line in enumerate(log_line, 1):
        clean_line = line.strip()
        if not clean_line:
            continue

        clean_log = line.split()

        if len(clean_log) < 3:
            print(f"{line_num}행 오류 발생 - {clean_line} 제외")
            continue

        date, test_name, result = clean_log[0], clean_log[1], clean_log[2].upper()

        if result not in ["PASS", "FAIL"]:
            print(f"{line_num}행 오류 - 결과값 확인 불가 '{result}' - {clean_line} 제외")
            continue

        total_test += 1

        if result == "PASS":
            total_pass += 1
        elif result == "FAIL":
            total_fail += 1
            fail_test.append({
                "date": date,
                "test_name": test_name,
                "log": clean_line
            })

    if total_test > 0:
        pass_rate = round((total_pass / total_test) * 100, 2)
        rate_str = f"{pass_rate}%"
    else:
        rate_str = "0.0%"

    result_data = {
        "summary":{
            "total_test": total_test,
            "total_pass": total_pass,
            "total_fail": total_fail,
            "pass_rate": rate_str
        },
        "fail_test": fail_test
    }

    try:
        with open(json_name, "w", encoding="utf-8") as f:
            json.dump(result_data, f, ensure_ascii=False, indent=4)
        print(f"'{json_name}' 파일 저장")
    except Exception as e:
        print(f"json 파일 저장 오류 - {e}")

    print(f"\n총 테스트 수 : {total_test}")
    print(f"성공 테스트 수 : {total_pass}")
    print(f"실패 테스트 수 : {total_fail}")
    print(f"성공률 : {rate_str}\n")

if __name__ == "__main__":
    parse_log()