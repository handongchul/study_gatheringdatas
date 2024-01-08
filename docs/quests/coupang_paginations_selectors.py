# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033&page=1
# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033&page=2
# ...
# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033&page=10

# * 웹 크롤링 동작
# * 웹 크롤링 동작
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
import time
# ChromeDriver 실행

from selenium.webdriver.chrome.options import Options

# Chrome 브라우저 옵션 생성
chrome_options = Options()

# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# WebDriver 생성
webdriver_manager_dricetory = ChromeDriverManager().install()

browser = webdriver.Chrome(service = ChromeService(webdriver_manager_directory), options=chrome_options)         # - chrome browser 열기

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities
pass

# for page_number in [1,2,3,4,5,6]:           # page number
for page_number in range(1,11):           # page number
    url = "https://www.coupang.com/np/campaigns/348?page={}".format(page_number)
    browser.get(url)                                     # - 주소 입력
    time.sleep(3)
    html = browser.page_source
    pass
pass    

                                                    # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                          # - html 파일 받음(and 확인)

from selenium.webdriver.common.by import By          # - 정보 획득


browser.quit()                                      # - 브라우저 종료
