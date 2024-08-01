# web crawling : 웹 페이지에서 원하는 정보(text, image, video)를 가져와서 수집하는 것

# 웹 크롤링을 할 때 저작권 문제가 발생할 수 있으니, 원래 상태의 데이터를 가공하여 사용하는 것이 좋다.

# 파이썬에서 웹 크롤링할 때 필수 유명 라이브러리 : beautyfulsoup4, selenium이 있다.
# beautyfulsoup4은 정적인 페이지를 크롤링할 때 편하게 사용할 수 있다.
# selenium은 동적인 페이지를 크롤링할 때 사용할 수 있다.

import requests
from bs4 import BeautifulSoup # bs4 패키지에서 beautifulsoup 클래스를 import
import pymysql

for i in range(1, 5) :
    targetUrl = 'https://www.lemite.com/product/list.html?cate_no=43&page=' + str(i) # page가 1부터 4까지 증가하도록 변수를 준다.



    headers = {'User-Agent' : 'Mozilla/5.0'} # 크롬 웹브라우저의 User-Agent를 headers에 붙여서 request를 보내려고 만든 것
    response = requests.get(targetUrl, headers=headers) 
    response.encoding = 'utf-8'
    html = response.text

    if html is not None :
        html = BeautifulSoup(html, 'html.parser') # BeautifulSoup 객체를 html로 parsing

        #prdList column4
        try : # 이거 해봐라
            products = html.find('ul', {'class' : 'prdList column4'})
        except : # 예외가 발생했다면 에러 메세지 띄워라
            print('Error : products not found')
        else : # 예외가 발생하지 않았다면 이거해라
            # print(products)
            products = products.find_all('li', {'class' : 'item xans-record-'})

            for product in products :
                # print(product)
                productDict = {}

                # 상품명
                productDict['prodName'] = product.find('p', {'class' : 'name'}).text.split(':')[1].strip()
                
                # 썸네일 이미지
                thumbImg = product.find('img', {'class' : 'thumb'}).attrs['src']
                if thumbImg.startswith('//'):
                    thumbImg = 'https:' + thumbImg
        
                productDict['thumbNail'] = thumbImg
                #productDict['thumbNail'] ='https:' + product.find('img',{'class' : 'thumb'}).attrs['src']
                print('---------------------------------------------------------------------------')

                # 상품번호
                productDict['prodNo'] = product.attrs['id'].split('_')[1].strip()
                print(productDict)

                # 판매가
                print(product.find('li', {'class' : 'xans-record-'}).next_sibling.next_sibling.text.split(':')[1].replace(',', '').replace('원', '').strip()) #  xans-record- 여기서 클래스명에 공백이 있어도 공백을 빼야한다  

                # 할인판매가
                print(product.find('li', {'class' : 'xans-record-'}).next_sibling.next_sibling.next_sibling.next_sibling.text)