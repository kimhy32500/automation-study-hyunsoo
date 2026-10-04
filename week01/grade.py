score = {"학생A" : 91, "학생B" : 81, "학생C" : 71, "학생D" : 61, "학생E" : 51}

while True:
    print("1. 학생 점수 목록")
    print("2. 학생 점수 수정")
    menu = input("숫자 입력 : ")
    print()

    if menu == "1":
        print("학생 목록 : ")

        for name, s in score.items():
            print(f"이름 : {name} / {s}점")

        average = sum(score.values()) / len(score)
        max_num = max(score.values())
        min_num = min(score.values())
        print()
        print("전체평균", average)
        print("최고점수 : ", max_num)
        print("최저점수 : ", min_num)
        print()

    elif menu == "2":
        name = input("학생 이름 입력 : ")

        if name == "학생A":
            new_score = input("학생A 수정할 점수 : ")

            if not new_score.isdigit():
                print("점수는 숫자 입력")

            else:
                score["학생A"] = int(new_score)
                print("학생A 점수 변경 완료")

        elif name == "학생B":
            new_score = input("학생B 수정할 점수 : ")

            if not new_score.isdigit():
                print("점수는 숫자 입력")

            else:
                score["학생B"] = int(new_score)
                print("학생B 점수 변경 완료")

        elif name == "학생C":
            new_score = input("학생C 수정할 점수 : ")

            if not new_score.isdigit():
                print("점수는 숫자 입력")

            else:
                score["학생C"] = int(new_score)
                print("학생C 점수 변경 완료")

        elif name == "학생D":
            new_score = input("학생D 수정할 점수 : ")

            if not new_score.isdigit():
                print("점수는 숫자 입력")

            else:
                score["학생D"] = int(new_score)
                print("학생D 점수 변경 완료")

        elif name == "학생E":
            new_score = input("학생E 수정할 점수 : ")

            if not new_score.isdigit():
                print("점수는 숫자 입력")

            else:
                score["학생E"] = int(new_score)
                print("학생E 점수 변경 완료")

        else:
            print("학생 이름 틀림")
            print()