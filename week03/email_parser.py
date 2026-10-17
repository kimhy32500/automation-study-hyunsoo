import json
import os

txt_name = "emails.txt"
json_name = "email_list.json"

def parse_email():
    if not os.path.exists(txt_name):
        print(f"{txt_name} 파일 없음.")
        return

    with open(txt_name, "r", encoding="utf-8") as f:
        email_list = f.readlines()

    pass_email = []
    fail_email = []
    domain_count = {}

    for email in email_list:
        clean_list = email.strip()
        if not clean_list:
            continue

        if clean_list.count("@") == 1:
            id, domain = clean_list.split("@", 1)

            if not id or not domain or "." not in domain:
                fail_email.append(clean_list)
                continue

            pass_email.append({
                "email": clean_list,
                "id": id,
                "domain": domain
            })

            if domain in domain_count:
                domain_count[domain] += 1
            else:
                domain_count[domain] = 1
        else:
            fail_email.append(clean_list)

    result_data = {
        "summary":{
            "total_pass": len(pass_email),
            "total_fail": len(fail_email),
            "domain_count": domain_count
        },
        "pass_email": pass_email,
        "fail_email": fail_email
    }

    with open(json_name, "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=4)

    print(f"{json_name} 저장 완료")

if __name__ == "__main__":
    parse_email()