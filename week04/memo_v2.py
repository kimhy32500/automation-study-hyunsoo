import json
import os
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

base_dir = Path(__file__).resolve().parent

load_dotenv(base_dir / ".env")

env_memo_path = os.getenv("MEMO_FILE_PATH")
if not env_memo_path or not env_memo_path.strip():
    memo_path = base_dir / "memo.json"
    print("환경 변수 없음으로 기본경로 사용")
else:
    memo_path = Path(env_memo_path)

if not memo_path.is_absolute():
    memo_path = base_dir / memo_path

if not memo_path.parent.exists():
    print(f"경로 오류 - '{memo_path.parent}' 폴더 없음")
    memo_path = base_dir / "memo.json"
    print("기본 경로(memo.json) 사용")

json_memo = str(memo_path)

def load_memo():
    if not os.path.exists(json_memo):
        return []

    try:
        with open(json_memo, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            print("메모 파일 데이터 형식 오류")
            return []

        valid_memo = []

        for item in data:
            if isinstance(item, dict) and all(k in item for k in ("id", "enter", "date")):
                valid_memo.append(item)
            else:
                print(f"형식 오류 메모 데이터 : {item}")

        return valid_memo

    except (json.JSONDecodeError, FileNotFoundError, PermissionError) as e:
        print(f"메모 파일 읽기 오류 {e}")
        return []

def save_memo(memo):
    try:
        with open(json_memo, "w", encoding="utf-8") as f:
            json.dump(memo, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"메모 저장 오류 : {e}")

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