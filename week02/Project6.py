def main():
    print("데이터 관리")

    data_list = []
    
    while True:
        print("1. 데이터 추가")
        print("2. 데이터 조회")
        print("3. 프로그램 종료")
        
        choice = input("선택: ").strip()
        
        if choice == "1":
            print("데이터 추가")
            item = input("추가할 데이터 입력 : ").strip()
            data_list.append(item)
            print(f"'{item}' 추가 완료")
        
        elif choice == "2":
            print("데이터 조회")
            
            if not data_list:
                print("-----------")
                print("저장된 데이터 없음")
                print("-----------")

            else:
                print("-----------")
                print("데이터 목록")
                for index, item in enumerate(data_list, start=1):
                    print(f"{index}. {item}")
                print("-----------")

        elif choice == "3":
            print("프로그램 종료")
            break
        
        else:
            print("1, 2, 3 숫자 입력")

if __name__ == "__main__":
    main()