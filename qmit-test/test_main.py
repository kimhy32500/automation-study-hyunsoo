from playwright.sync_api import Page, expect

URL = "https://v369.dev.l-walk.com"

def test_메인_페이지_타이틀(page: Page):
    page.goto(URL)
    expect(page).to_have_title("큐밋! SW 테스트 프로젝트 아웃소싱 플랫폼")

def test_성공_사례_버튼이_보인다(page: Page):
    page.goto(URL)
    expect(page.get_by_role("link", name="성공 사례")).to_be_visible()

def test_성공_사례_버튼을_누른다(page: Page):
    page.goto(URL)
    success = page.get_by_role("link", name="성공 사례")
    success.click()

def test_성공_사례_화면_확인(page: Page):
    page.goto(URL)
    success = page.get_by_role("link", name="성공 사례")
    success.click()
    page_btn = page.locator("button.paginate-buttons.active-page").get_by_text("1")
    expect(page_btn).to_be_visible()

def test_성공_사례_등록된_글_갯수_확인(page: Page):
    page.goto(URL)
    success = page.get_by_role("link", name="성공 사례")
    success.click()
    posts = page.locator(".q-card-container")
    expect(posts.first).to_be_visible()
    
    count = posts.count()
    print(f"현재 등록된 성공 사례 글 개수: {count}")
    
    assert count > 0, "성공 사례 게시글 없음"