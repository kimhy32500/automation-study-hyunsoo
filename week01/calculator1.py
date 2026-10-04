a = input("숫자 입력 1 : ")
while not a.isdigit():
    print("숫자만 입력")
    a = input("숫자 입력 1 : ")
a = int(a)

b = input("숫자 입력 2 : ")
while not b.isdigit() or b == "0":
    if not b.isdigit():
        print("숫자만 입력")
    elif b == "0":
        print("0 이외 숫자 입력")
    b = input("숫자 입력 2 : ")
b = int(b)

print("더하기 : ", a+b)
print("빼기 : ", a-b)
print("곱하기 : ", a*b)
print("나누기 : ", a/b)