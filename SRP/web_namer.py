import requests
from bs4 import BeautifulSoup

url = "https://www.edureka.co/blog/web-scraping-with-python/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

elements = soup.find_all(True)
for element in elements:
    print(f"Element name: {element.name}")
    print(f"Element id: {element.get('id')}")
    print(f"Element class: {element.get('class')}")
    print(f"Element href: {element.get('href')}")
    print(f"Element src: {element.get('src')}")
    print(f"Element alt: {element.get('alt')}")
    print(f"Element value: {element.get('value')}")
    print("------------------")