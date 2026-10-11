def gugudan(number):
    print(f"{number}단")
    for i in range(1,10):
        result = number * i
        print(f"{number} X {i} = {result}")

def main():
    while True:
        input_number = input("숫자 입력 : ")

        if input_number.isdigit():
            number = int(input_number)
            gugudan(number)
            break

        else:
            print("숫자를 입력해야합니다.")

if __name__ == "__main__":
    main()