from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC # 웹드라이브에서 예외처리할 때 사용하는 라이브러리
from selenium.webdriver import ActionChains # 스크롤바를 제어하는 라이브러리
from selenium.webdriver.common.by import By

import time

import pandas as pd

# 스타벅스의 홈페이지에서 매장의 이름, 주소, 구 이름, 위도, 경도를 크롤링 해와서 csv, DataFrame으로 만들자.
driver = webdriver.Chrome()
driver.get('https://www.starbucks.co.kr/store/store_map.do')
driver.maximize_window() # 사이즈를 최대화
time.sleep(3)

# 모달창 닫기
driver.find_element(By.XPATH, '/html/body/div[4]/p/a').click()
time.sleep(3)

# 지역 검색 버튼 누르기
driver.find_element(By.XPATH, '//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/header[2]/h3/a').click()
time.sleep(1)

# 서울 클릭
driver.find_element(By.XPATH, '//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[1]/a').click()
time.sleep(1)

# 전체 클릭
driver.find_element(By.XPATH, '//*[@id="mCSB_2_container"]/ul/li[1]/a').click()
time.sleep(7) # 전체를 가져오려면 로딩이 걸리기 때문에 7초 정도 시간을 줘야한다.

# 전체 매장의 Ul 태그
stores = driver.find_element(By.XPATH, '//*[@id="mCSB_3_container"]/ul')
store_list = stores.find_elements(By.TAG_NAME, 'li')

# print(len(store_list)) : 616개가 나와야 한다.

# css 때문에 화면에 보여지는 4개의 매장 이름만 가지고 온다.
# 따라서 스크롤바를 제어해줘야 한다.
action = ActionChains(driver)

starbucks_list = []

for i in range(0, len(store_list)) :
    store = store_list[i]

    # store 가리키는 태그가 보이도록 스크롤바를 움직이게 한다.
    action.move_to_element(store).perform()
    
    # 매장 이름 찾기 
    name = store.find_element(By.XPATH, '//*[@id="mCSB_3_container"]/ul/li[' + str(i+1) + ']/strong').text.strip()
    # 0번째 매장이 아니라 1번째 매장부터 시작하므로 i에 1을 더해준다.

    # 주소 크롤링
    address = store.find_element(By.XPATH, '//*[@id="mCSB_3_container"]/ul/li[' + str(i+1) +']/p').text.strip()
    address = address.replace('1522-3232', '') # 대표전화라서 모든 번호가 똑같기 때문에 없애준다.
    address = address.replace('\n', '') # 주소와 번호 사이에 엔터가 있어서 그것도 없애준다.
    
    # 구 이름 크롤링
    gu = address.split(' ')[1]

    # 위도, 경도 크롤링 get_attribute : 속성 가져오는 함수
    lat = store.get_attribute('data-lat')
    long = store.get_attribute('data-long')

    # DataFrame으로 만들기 위해 하나의 매장 정보를 Dictionary로 만들어준다.
    store_info = {
        '브랜드' : '스타벅스',
        '상호명' : name,
        '구' : gu,
        '주소' : address,
        '위도' : lat,
        '경도' : long
    }

    starbucks_list.append(store_info)
    print(store_info)
    print('----------------------------------------------------------------------------------------')

# DataFrame으로 변환
df_starbucks = pd.DataFrame(starbucks_list)
print(df_starbucks)

# csv로 저장
df_starbucks.to_csv('starbucks.csv')
