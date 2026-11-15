members = {
    "1": ["가가가", "20", "서울"],
    "2": ["나나나", "21", "서울"],
    "3": ["다다", "30", "경기"],
    "4": ["라라라", "25", "인천"],
    "5": ["마마마", "34", "부산"],
    "6": ["바바바", "28", "대구"],
    "7": ["사사사", "31", "광주"],
    "8": ["아아아", "22", "대전"],
    "9": ["자자", "29", "울산"],
    "10": ["차", "40", "세종"]
}

while True:
    print("1. 회원 목록")
    print("2. 회원 정보 수정")
    menu = input("숫자 입력 : ")
    print()

    if menu == "1":
        print("회원 목록 : ")
        print()

        while True:
            print("1. 전체 회원 목록")
            print("2. 30세 이상 회원 정보")
            menu = input("숫자 입력 : ")
            print()

            if menu == "1":
                print("회원 목록 : ")

                for id,info in members.items():
                    print(f"[{id}번] 이름: {info[0]} | 나이: {info[1]}세 | 지역: {info[2]}")
                    print()
                break

            elif menu == "2":
                print("30세 이상 회원 목록 : ")

                for id,info in members.items():

                    if int(info[1]) >= 30:
                        print(f"[{id}번] 이름: {info[0]} | 나이: {info[1]}세 | 지역: {info[2]}")
                        print()

                break

    elif menu == "2":
        name = input("회원 이름 입력 : ")

        for id,info in members.items():
            if info[0] == name:
                new_name = input("수정할 이름 입력 : ")
                new_age = input("수정할 나이 입력 : ")

                if not new_age.isdigit():
                    print("숫자만 입력 가능")
                    break

                new_area = input("수정할 지역 입력 : ")

                members[id] = [new_name, new_age, new_area]

                print("회원 정보 변경 완료")
                print()
                break

        else:
            print("회원 이름 틀림")
            print()