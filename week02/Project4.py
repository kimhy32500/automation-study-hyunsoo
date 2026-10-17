def validate_password(password):

    password = password.strip()

    if len(password) < 8:
        return False, "비밀번호는 8자 이상"

    alpha = False
    digit = False

    for char in password:
        if char.isalpha():
            alpha = True
        elif char.isdigit():
            digit = True

    if not alpha:
        return False, "비밀번호에 영문자가 최소 1개 이상 포함 필요"
        
    if not digit:
        return False, "비밀번호에 숫자가 최소 1개 이상 포함 필요"

    return True, "사용 가능 비밀번호 입력 완료"

def main():

    while True:
        while True:
            pwd1 = input("비밀번호 입력(8자 이상, 영문/숫자 포함): ").strip()
            
            valid, message = validate_password(pwd1)

            if valid:
                print("1차 비밀번호 입력 완료")
                print()
                break
            else:
                print(f"{message}")
            
        pwd2 = input("비밀번호 확인을 위해 다시 입력하세요: ").strip()
        
        if pwd1 == pwd2:
            print("비밀번호 설정 완료")
            print()
            break
        else:
            print("비밀번호 불일치. 처음부터 다시 입력")
            print()

if __name__ == "__main__":
    main()