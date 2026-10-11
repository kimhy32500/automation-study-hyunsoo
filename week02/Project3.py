def count_word(word):
    words = word.strip().lower().split()

    enter_words = {}

    for text in words:
        enter_words[text] = enter_words.get(text, 0) + 1

    return enter_words

def main():
    example_text = "Studying Python for test automation is hard, but studying automation with Python is worth it."

    print(f"예시 문장 : {example_text}")

    result = count_word(example_text)

    print("단어 빈도 계산")
    for word, count in result.items():
        print(f"'{word}' : {count}회")

if __name__ == "__main__":
    main()