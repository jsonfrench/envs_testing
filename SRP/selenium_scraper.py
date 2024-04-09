from selenium import webdriver
from bs4 import BeautifulSoup


URL = "https://grants.nih.gov/grants/guide/notice-files/NOT-HD-23-023.html"
driver = webdriver.Chrome()

driver.get(URL)

driver.implicitly_wait(10)

page_source = driver.page_source
driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')

abstract_element = soup.find('div', class_='data highlight-text')

abstract_text = abstract_element.get_text(strip=True)

print(abstract_text)
