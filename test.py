import requests
from bs4 import BeautifulSoup
href = "https://blog.naver.com/PostView.nhn?blogId=airumeraru&logNo=221365616574"
source = requests.get(href).text
soup = BeautifulSoup(source,'lxml')
soup = soup.find_all('div', {'class', 'se_textView'})
for a in soup:
    print(a.get_text())