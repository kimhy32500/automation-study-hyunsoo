import json
import os
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

base_dir = Path(__file__).resolve().parent

load_dotenv(base_dir / ".env")

memo_path = Path(os.getenv("MEMO_FILE_PATH", "memo.json"))

if not memo_path.is_absolute():
    memo_path = base_dir / memo_path

json_memo = str(memo_path)

def load_memo():
    if not os.path.exists(json_memo):
        return []

    try:
        with open(json_memo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print("json 리스트 없음")
        return []

def save_memo(memo):
    with open(json_memo, "w", encoding="utf-8") as f:
        json.dump(memo, f, ensure_ascii=False, indent=4)

def memo_main():
    memo = load_memo()

    while True:
        print("\n1. 메모 추가")
        print("2. 메모 조회")
        print("3. 메모 검색")
        print("4. 종료\n")

        selete = input("번호 입력: ").strip()

        if selete == "1":
            enter_memo = input("메모 작성 : ").strip()
            if not enter_memo:
                print("메모 미입력으로 추가 불가\n")
                continue
            memo_id = len(memo) +1
            create_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            memo_item = {
                "id": memo_id,
                "enter": enter_memo,
                "date": create_date
            }
            memo.append(memo_item)
            save_memo(memo)
            print("메모 저장 완료\n")

        elif selete == "2":
            if not memo:
                print("저장된 메모 없음\n")
                continue

            print("[메모 목록]")
            for item in memo:
                print(f"[{item['id']}] : {item['enter']} - {item['date']}")

        elif selete == "3":
            serch = input("검색어 입력 : ").strip()
            if not serch:
                print("검색어 미입력으로 검색 불가\n")
                continue

            result = [item for item in memo if serch in item['enter']]

            if not result:
                print("검색 결과 없음\n")
            else:
                print(f"검색 결과 [{len(result)}개]")
                for item in result:
                    print(f"[{item['id']}] : {item['enter']} - {item['date']}")

        elif selete == "4":
            save_memo(memo)
            print("프로그램 종료")
            break

        else:
            print("1~4 숫자 입력")

if __name__ == "__main__":
    memo_main()