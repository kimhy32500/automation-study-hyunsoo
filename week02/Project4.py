def validate_password(password):
    if len(password) < 4:
        return False, "비밀번호는 4자 이상"

    word = False
    number = False

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in password:
        if char in alphabet:
            word = True
        elif char.isdigit():
            number = True

    if not word:
        return False, "비밀번호에 영문자가 최소 1개 이상 포함 필요"
        
    if not number:
        return False, "비밀번호에 숫자가 최소 1개 이상 포함 필요"

    return True, "사용 가능 비밀번호 입력 완료"

def main():

    for _ in iter(int, 1):
        
        for _ in iter(int, 1):
            pwd1 = input("비밀번호 입력(4자 이상, 영문/숫자 포함): ")
            
            valid, message = validate_password(pwd1)

            if valid:
                print("1차 비밀번호 입력 완료")
                break
            else:
                print(f"{message}")
            
        pwd2 = input("비밀번호 확인을 위해 다시 입력하세요: ")
        
        if pwd1 == pwd2:
            print("비밀번호 설정 완료")
            break
        else:
            print("비밀번호 불일치. 처음부터 다시 입력")

if __name__ == "__main__":
    main()