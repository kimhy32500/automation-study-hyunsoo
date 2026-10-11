import string_utils

def main():
    name_list = ["  김David  ", "ALICE박 ", "  서지우 ", "david 김 ", "   Bob  ", "박도현  ", "  charlie최 ", "이서윤 ", "  Eve  ", "  정하준 smith "]

    print(", ".join(name_list))

    delete_space_name = []

    for name in name_list:
        refrash_name = string_utils.space_delete(name)
        delete_space_name.append(refrash_name)

    delete_space_name.sort()

    print("이름 목록 정리 : ")
    for index, name in enumerate(delete_space_name, start=1):
        print(f"{index}. {name}")

if __name__ == "__main__":
    main()