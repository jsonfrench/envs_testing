import requests
from bs4 import BeautifulSoup

# URL of the NIH projects website
url = "https://reporter.nih.gov/search/tox8NNrrKEq8vl9E9mPP3g/project-details/10751444"

# Send a GET request to the website and get the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the project links on the page
project_links = soup.find_all('a', class_='proj_list_title')

# Iterate over each project link and download the abstract text
for link in project_links:
    project_url = link['href']
    project_response = requests.get(project_url)
    project_soup = BeautifulSoup(project_response.content, 'html.parser')
    
    # Find the abstract text on the project page
    abstract = project_soup.find('div', class_='proj_abstract')
    abstract_text = abstract.get_text(strip=True)
    
    # Do whatever you want with the abstract text (e.g., save it to a file, print it)
    print(abstract_text)