# 셀레니움 라이브러리를 이용하여 웹 크롤링을 해보기
# 셀레니움은 Selenium WebDriver를 Python으로 wrapping한 library로, 웹 브라우저를 제어할 수 있게 해준다.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service # 크롬의 웹 브라우저를 실제로 구동시키는 객체
# 크롬 웹 브라우저의 driver를 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True) # 크롬 웹 브라우저의 꺼짐을 방지
chrome_options.add_argument("--start-maximized") # 크롬 웹 브라우저의 크기를 최대화하는 옵션 / 반응형 웹 브라우저는 크기가 줄어들면 모바일 버전으로 바뀌기 때문임

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 해당 웹 주소로 이동
driver.get('https://www.naver.com/')

driver.implicitly_wait(10) # 10초 동안 대기, 위의 페이지가 로딩이 되어야 밑에 불러온 태그를 충분한 시간 안에 불러올 수 있다.

# #shortcutArea > ul > li:nth-child(4) > a > span.service_icon.type_shopping
driver.find_element(By.CSS_SELECTOR, '#shortcutArea > ul > li:nth-child(4) > a > span.service_icon.type_shopping').click()

driver.implicitly_wait(20) # 20초 동안 대기

# print(driver.title) # 네이버


# 쇼핑 페이지가 새로운 탭에서 열렸으므로, 드라이버를 해당 탭으로 전환해야 한다.
driver.switch_to.window(driver.window_handles[-1]) # 0번 : 네이버 홈 / 1번 : 쇼핑 페이지 -> 끝에서 보면 쇼핑 페이지가 -1번째 페이지다.
# print(driver.title) # 네이버 쇼핑

driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/button[2]').click()

# //*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input
searchBox = driver.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')

searchBox.click()
searchBox.send_keys('짱구 인형')
searchBox.send_keys(Keys.ENTER)
driver.implicitly_wait(100) # 20초 동안 대기