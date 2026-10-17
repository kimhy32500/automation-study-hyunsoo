def space_delete (word):
    return word.strip().lower()

def check_mail(email):
    email = email.strip()
    if email.count("@") != 1:
        return False

    id, domain = email.split("@")

    if not id or not domain or "." not in domain:
        return False

    return True

def masking_mail(email):
    if not check_mail(email):
        return "메일 형식 아님"

    id, domain = email.strip().split("@")

    if len(id) > 3:
        masking_id = id[:3] + "*" *(len(id) - 3)
    else:
        masking_id = id[0] + "*" *(len(id) - 1)
    return f"{masking_id}@{domain}"

def check_count(words):
    words = words.strip().split()
    return len(words)

def reverse_word(words):
    return words.strip()[::-1] 