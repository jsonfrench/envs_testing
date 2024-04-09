import requests
from bs4 import BeautifulSoup

#URL = "https://reporter.nih.gov/search/tox8NNrrKEq8vl9E9mPP3g/project-details/10751444"
#URL = "https://grants.nih.gov/grants/guide/notice-files/NOT-HD-23-023.html"
URL = "https://reporter.nih.gov/search/tox8NNrrKEq8vl9E9mPP3g/project-details/10751444.html"

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# Find the abstract text element
abstract_element = soup.find('div', class_='data highlight-text')
#abstract_element = soup.find('span', class_='mw-headline')
# abstract_text = abstract_element.get_text(strip=True)

#print(soup.get_text)
print(abstract_element.get_text())
