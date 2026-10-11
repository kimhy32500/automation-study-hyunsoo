import string_utils

def main():
    sample_text = "  weeK02     "
    sample_email = "testiD123@test.cOm"
    sanple_grammar = "I'm doing study automation"

    delete_space = string_utils.space_delete(sample_text)
    print(f"공백 제거와 소문자 변환 '{delete_space}'")

    check_domain = string_utils.check_mail(sample_email)
    print(f"도메인 체크 '{check_domain}'")

    masking_id = string_utils.masking_mail(sample_email)
    print(f"마스킹처리 '{masking_id}'")

    count_word = string_utils.check_count(sanple_grammar)
    print(f"Text 카운트 : '{count_word}'")

    reversed_word = string_utils.reverse_word(sample_text)
    print(f"문자열 반대로 : '{reversed_word}'")

if __name__ == "__main__":
    main()