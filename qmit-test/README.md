# Playwright 1주차 과제 - 돌아가는 테스트 프로젝트 만들기

## 1. 프로젝트 개요
- 작업 경로: `C:\Users\kimhy\Documents\automation-study-hyunsoo`
- 테스트 대상 사이트: `https://v369.dev.l-walk.com`
- 사용 기술 스택: Python, Pytest, Playwright (`pytest-playwright`)

---

## 2. 디렉토리 구조 및 파일 구성
- `qmit-test/test_main.py`: 테스트 스크립트
- `requirements.txt`: 프로젝트 의존성 고정 파일
- `README.md`: 과제 수행 결과 리포트

---

## 3. 의존성 관리
가상환경 내 패키지 버전 고정 명령어:
python -m pip freeze > requirements.txt

---

## 4. 테스트 시나리오
- 메인 페이지 타이틀 확인
- 성공 사례 버튼 노출 확인
- 버튼 클릭 동작 확인
- 성공 사례 화면 이동 확인
- 등록된 글 개수 확인
테스트 작성 완료.

---

## 5. 크로스 브라우저 테스트 결과
- Chromium 및 Firefox 환경에서 5개 테스트 항목 모두 통과 (PASS).
- WebKit은 Windows 보안으로 실행 불가.
- 실행 명령어:
  python -m pytest -v
  python -m pytest -v --browser firefox

---

## 6. 테스트 실패 로그 실습
- 타이틀 검증 항목을 일부러 틀리게 수정하여 실행한 실패 로그:
  - Expected: `큐밋! SW 테스트 프로젝트 아웃소싱 플랫폼 - 틀린값`
  - Actual: `큐밋! SW 테스트 프로젝트 아웃소싱 플랫폼`
  - 로그: `AssertionError: Page title expected to be '큐밋! SW 테스트 프로젝트 아웃소싱 플랫폼 - 틀린값'`
- 실습 직후 코드는 정상 값으로 원복 완료.

---

## 7. URL 하드코딩 현황
- 하드코딩 개수: 1군데 (`URL = "https://v369.dev.l-walk.com"` 상단 변수 선언)
- 각 테스트 함수에서 해당 변수를 참조하여 사용 중

## 8. 문의사항
pytest 실행 시

======================================================================================================== warnings summary =========================================================================================================
qmit-test/test_main.py::test_메인_페이지_타이틀[chromium]
  C:\Users\kimhy\Documents\automation-study-hyunsoo\.venv\Lib\site-packages\_pytest\fixtures.py:1392: PytestRemovedIn10Warning: Session-scoped fixtures defined as instance methods are deprecated.
  Instance attributes set in the 'base_url' fixture will NOT be visible to test methods,
  as each test gets a new instance while the fixture runs only once per class.
  Use a @classmethod decorator below @pytest.fixture and set attributes on cls instead.
  See https://docs.pytest.org/en/stable/deprecations.html#class-scoped-fixture-as-instance-method
    fixturefunc = resolve_fixture_function(fixturedef, request)

1. 위 내용의 warnings summary가 출력되는데 신경쓰지 않아도 되는건가요?
2. WebKit는 window 환경에서 실행이 안되는데 따로 실행 방법이 있는지건가요?