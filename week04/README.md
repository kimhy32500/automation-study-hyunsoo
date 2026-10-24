# Week 04 - 환경 설정 및 메모 프로그램

## 1. 실행환경 준비 방법

Python이 설치되어 있어야 합니다.

프로젝트 루트에서 `week04` 폴더로 이동합니다.

```powershell
cd week04
```

가상환경을 생성합니다.

```powershell
python -m venv .venv
```

가상환경을 활성화합니다.

```powershell
.\.venv\Scripts\Activate.ps1
```

터미널에 `(.venv)`가 표시되면 가상환경이 활성화된 상태입니다.

## 2. 필요한 라이브러리 설치 방법

가상환경이 활성화된 상태에서 다음 명령어를 실행합니다.

```powershell
python -m pip install -r requirements.txt
```

`requirements.txt`에 명시된 `python-dotenv` 라이브러리가 설치됩니다.

## 3. 환경설정 준비 방법

`week04` 폴더에서 `.env.example` 파일을 복사하여 `.env` 파일을 생성합니다.

```powershell
Copy-Item .env.example .env
```

`.env` 파일을 열고 필요한 환경변수를 설정합니다.

```dotenv
MEMO_FILE_PATH=memo.json

LOGIN_ID=your_login_id
LOGIN_PASSWORD=your_password
BASE_URL=https://example.com
```

- `MEMO_FILE_PATH`: 메모 데이터가 저장될 JSON 파일 경로
- `LOGIN_ID`: 예제 로그인 ID
- `LOGIN_PASSWORD`: 예제 비밀번호
- `BASE_URL`: 예제 기본 URL

실제 사용할 값에 맞게 수정합니다. 비밀번호는 프로그램에서 마스킹하여 출력합니다.

`MEMO_FILE_PATH`가 설정되지 않으면 기본 파일인 `memo.json`을 사용합니다. 상대 경로는 `memo_v2.py`가 있는 `week04` 폴더를 기준으로 합니다.

`.env` 파일에는 개인 환경설정이 포함될 수 있으므로 GitHub에 업로드하지 않습니다.

## 4. 프로그램 실행 방법

### 환경설정 확인 프로그램

`week04` 폴더에서 다음 명령어를 실행합니다.

```powershell
python config_demo.py
```

환경변수를 불러오고 필수 설정값의 누락 여부를 확인합니다. 비밀번호는 마스킹하여 출력합니다.

### 메모 프로그램

다음 명령어를 실행합니다.

```powershell
python memo_v2.py
```

프로그램 메뉴에서 원하는 기능을 선택합니다.

1. 메모 추가
2. 메모 조회
3. 메모 검색
4. 종료

메모 데이터는 설정한 경로의 JSON 파일에 저장됩니다.
