import requests
from bs4 import BeautifulSoup
import openpyxl

#URL = "https://grants.nih.gov/grants/guide/rfa-files/RFA-AA-23-001.html"
URL = "https://grants.nih.gov/grants/guide/rfa-files/RFA-OD-21-006.html"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html")
q=soup.get_text() #all text for FOA

#remove first occurances of these
t = q.replace("Part 2. Full Text of Announcement","",1)
t = t.replace("Section II. Award Information","",1)

#reduce text to title, purpose, and full announcement text, 
u=t[t.find("Funding Opportunity Title"):t.find("Activity Code")]
v=t[t.find("Funding Opportunity Purpose"):t.find("Key Dates")]
w=t[t.find("Part 2. Full Text of Announcement"):t.find("Section II. Award Information")]
x = u+v+w 
y = x.replace("\t", " ")
z = y.replace("\n", " ") #you may need to remove additional \n 

print(z) 
