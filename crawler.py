from bs4 import BeautifulSoup
import requests
i = 1
count = 1
file = open('data/naver_question/test/data.txt', 'w+')
while i <= 100:
    print(i)
    response = requests.get('https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query=서울 카페 추천&sm=tab_pge&kin_start='+str(10*(i-1)+1))
    soup = BeautifulSoup(response.text, 'lxml')
    a = soup.find(id='elThumbnailResultArea')
    for b in a.find_all('dt', {'class':'question'}):
        print(count)
        question_href = b.a['href']
        response = requests.get(question_href)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            file.write(str(count)+". "+str(soup.find('div', {'class':'c-heading__content'}).get_text()))
        except:
            print('error')
        count +=1
    i+=1

