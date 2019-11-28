from bs4 import BeautifulSoup
import requests, sys, os

print("NaverPlaceBlogCrawler started")

place_id = sys.argv[1]
place_name = sys.argv[2]
try:
    max_count = int(sys.argv[3])
except:
    max_count = 10
data_save_path = "data/NaverPlaceBlogCrawler/"+place_name
if not os.path.exists(data_save_path):
    os.mkdir(data_save_path)

file = open(data_save_path+'/data.txt', 'w+')

count = 1
i = 1
while count <= max_count:
    response = requests.get('https://store.naver.com/restaurants/detail?id='+place_id+'&tab=fsasReview&tabPage='+str(i))
    soup = BeautifulSoup(response.text, 'lxml')
    a = soup.find('ul', {'class': 'list_place_col1'})
    if a == None:
        break
    for b in a.find_all('div', {'class':'list_item_inner'}):

        print(str(count) + " item started")
        blog_href = str(b.a['href'])
        if not blog_href.split('/')[2].split('.')[0]== "blog":
            print(blog_href)
            continue
        blog_id = blog_href.split('/')[3]
        post_id = blog_href.split('/')[4]
        blog_href = "https://blog.naver.com/PostView.nhn?blogId="+blog_id+"&logNo="+post_id
        source = requests.get(blog_href).text
        blog_soup = BeautifulSoup(source, 'lxml')
        text_areas = blog_soup.find_all('div', {'class', 'se-module-text'})
        file.write(str(count)+". ")
        file.write(blog_href+"/n")
        if len(text_areas) == 0:
            text_areas = blog_soup.find_all('div', {'class', 'se_textView'})
        if len(text_areas) == 0 :
            print(blog_href)
        for text_part in text_areas:
            file.write(text_part.get_text()+"\n")
        file.write("\n")
        # try:
        #     file.write(str(count)+". "+str(b.get_text())+"\n")
        # except:
        #     print('error')
        count +=1
    i+=1

print("NaverPlaceBlogCrawler ended")

