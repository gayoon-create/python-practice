# 셀레니움을 이용하여
# https://ncov.kdca.go.kr/pot/index.do 사이트로 이동 후
# 감염병 주요 뉴스 메뉴를 클릭하게 하고
# 뉴스에 "확진자" 검색 후 나오는 게시글의 제목을 추출하여 list에 넣고 출력

import requests
from bs4 import BeautifulSoup

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
driver.get('https://ncov.kdca.go.kr/pot/index.do')

driver.implicitly_wait(10) # 10초 동안 대기, 위의 페이지가 로딩이 되어야 밑에 불러온 태그를 충분한 시간 안에 불러올 수 있다.

# //*[@id="gnb"]/div/ul/li[2]/a (전체메뉴 클릭)
driver.find_element(By.XPATH, '//*[@id="gnb"]/div/ul/li[2]/a').click()
driver.implicitly_wait(20) # 20초 동안 대기

# //*[@id="modal-menu"]/div[1]/div[2]/div[2]/ul/li[1]/a (감염병 주요뉴스 탭 클릭)
driver.switch_to.window(driver.window_handles[-1])
driver.find_element(By.XPATH, '//*[@id="modal-menu"]/div[1]/div[2]/div[2]/ul/li[1]/a').click()
driver.implicitly_wait(20) # 20초 동안 대기

# //*[@id="q_searchVal"] ("확진자" 검색어 입력)
searchBox = driver.find_element(By.XPATH, '//*[@id="q_searchVal"]')
searchBox.click()
searchBox.send_keys('확진자')
searchBox.send_keys(Keys.ENTER)
driver.implicitly_wait(100) # 20초 동안 대기

# for i in range(1, 2): #  page 포함, 미만
#     targetUrl = 'https://ncov.kdca.go.kr/pot/bbs/BD_selectBbsList.do?q_bbsSn=1008&q_bbsDocNo=&q_clsfNo=&q_searchKeyTy=&q_searchVal=%ED%99%95%EC%A7%84%EC%9E%90&q_currPage='+ str(i) + '&q_sortName=&q_sortOrder=' # url page number

#     headers = {'User-Agent': 'Mozilla/5.0'} # 크롭 웹브라우저의  user-agent에 붙여서 request를 보내려고
#     responese = requests.get(targetUrl, headers=headers)
#     responese.encoding = 'utf-8'
#     html = responese.text

#     if html:
#         soup = BeautifulSoup(html, 'html.parser')  # HTML을 parsing하여 DOM 구조로 변환

#         try:  # 예외 처리
#             rows = soup.find_all('tr')
#             if not rows:
#                 raise ValueError('No rows found')

#             for row in rows:
#                 title_cell = row.find('td', {'class': 'cell-subject'})
#                 if title_cell:
#                     title = title_cell.get_text(strip=True)
#                     print('Title:', title)

#         except Exception as e:  # 예외가 발생했다면
#             print('Error:', str(e))

for i in range(1, 11):
    # 뉴스에 "확진자" 검색 후 나오는 게시글의 제목을 추출하여 list에 넣으시고, 출력하세요
    titles={}
    titles[i] = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/table/tbody/tr['+str(i)+']/td[2]/a').get_property('innerText')
    print(titles)
