# 데이터 스크래핑
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServiece
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from lxml import html
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-gpu")
# chrome_options.binary_location = "usr/bin/google-chrome-stable"

driver = webdriver.Chrome(options=chrome_options)

url = "https://www.naver.com"
driver.get(url)
time.sleep(2)

print(driver.page_source)
page_source = driver.page_source
tree = html.fromstring(page_source)

try:
    title_text = tree.xpath("//title/text()")
    print("웹페이지 제목 (XPath): ", title_text[0] if title_text else "제목 없음")
except Exception as e:
    print(f"XPath 추출 실패: {e}")

driver.quit()
