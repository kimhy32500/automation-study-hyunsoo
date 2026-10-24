import os
from pathlib import Path
from dotenv import load_dotenv

def load_config():
    base_dir = Path(__file__).resolve().parent
    load_dotenv(base_dir / ".env")

    config = {
        "login_id": os.getenv("LOGIN_ID"),
        "login_pwd": os.getenv("LOGIN_PASSWORD"),
        "base_url": os.getenv("BASE_URL")
    }

    return config

def validate_config(config):
    miss_settings = []

    for key , value in config.items():
        if not value or not value.strip():
            miss_settings.append(key)

    return miss_settings

def print_config(config):
    print("환경설정 정보")
    print(f"로그인 ID: {config['login_id']}")

    login_pwd = config['login_pwd']

    if len(login_pwd) > 1:
        masked_pwd = login_pwd[0] + "*" * (len(login_pwd) - 1)
    else:
        masked_pwd = "*"

    print(f"비밀번호: {masked_pwd}")
    print(f"기본 URL: {config['base_url']}")

def main():
    try:
        config = load_config()
        miss_settings = validate_config(config)

        if miss_settings:
            raise ValueError(
                "필수 환경 설정 누락: " + ", ".join(miss_settings)
            )
        print_config(config)

    except ValueError as e:
        print(f"환경설정 오류 - {e}")

if __name__ == "__main__":
    main()