import string_utils

def main():
    sample_text = "  weeK02     "
    sample_email = "testiD123@test.cOm"
    invalid_email1 = "a@b@c.com"
    invalid_email2 = "@test.com"  
    sanple_grammar = "I'm doing study automation"

    delete_space = string_utils.space_delete(sample_text)
    print(f"공백 제거와 소문자 변환 '{delete_space}'")
    print()    

    check_domain = string_utils.check_mail(sample_email)
    print(f"도메인 체크 '{check_domain}'")
    invalid_domain1 = string_utils.check_mail(invalid_email1)
    print(f"예외 도메인 체크1 '{invalid_domain1}'")
    invalid_domain2 = string_utils.check_mail(invalid_email2)
    print(f"예외 도메인 체크2 '{invalid_domain2}'")
    print()

    masking_id = string_utils.masking_mail(sample_email)
    print(f"마스킹 처리 '{masking_id}'")
    invalid_masking_domain1 = string_utils.masking_mail(invalid_email1)
    print(f"예외 마스킹 처리1 '{invalid_masking_domain1}'")
    invalid_masking_domain2 = string_utils.masking_mail(invalid_email2)
    print(f"예외 마스킹 체크2 '{invalid_masking_domain2}'")
    print()

    count_word = string_utils.check_count(sanple_grammar)
    print(f"Text 카운트 : '{count_word}'")
    print()
    
    reversed_word = string_utils.reverse_word(sample_text)
    print(f"문자열 반대로 : '{reversed_word}'")
    print()

if __name__ == "__main__":
    main()