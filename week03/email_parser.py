import json
import os

txt_name = "emails.txt"
json_name = "email_list.json"


def validate_email(email):
    if any(char.isspace() for char in email):
        return False

    if email.count("@") != 1:
        return False

    id, domain = email.split("@", 1)

    if not id or not domain:
        return False

    if id.startswith(".") or id.endswith("."):
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    if ".." in id or ".." in domain:
        return False

    if "." not in domain:
        return False

    return True

def read_email():
    if not os.path.exists(txt_name):
        print(f"{txt_name} 파일 없음")
        return None

    with open(txt_name, "r", encoding="utf-8") as f:
        email_list = f.readlines()

    return email_list

def check_email(email_list):
    pass_email = []
    fail_email = []
    domain_count = {}

    for email in email_list:
        clean_list = email.strip("\r\n")

        if not clean_list.strip():
            continue

        if not validate_email(clean_list):
            fail_email.append(clean_list)
            continue

        id,domain = clean_list.split("@", 1)

        pass_email.append({
            "email": clean_list,
            "id": id,
            "domain": domain
        })

        if domain in domain_count:
            domain_count[domain] += 1
        else:
            domain_count[domain] = 1

    result_data = {
        "summary": {
            "total_pass": len(pass_email),
            "total_fail": len(fail_email),
            "domain_count": domain_count
        },
        "pass_email": pass_email,
        "fail_email": fail_email
    }
    return result_data

def save_result(result_data):
    with open(json_name, "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=4)

    print(f"{json_name} 저장 완료")

def parse_email():
    email_list = read_email()

    if email_list is None:
        return

    result_data = check_email(email_list)
    save_result(result_data)

if __name__ == "__main__":
    parse_email()