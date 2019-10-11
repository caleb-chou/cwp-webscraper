import requests
from bs4 import BeautifulSoup
import os
import re

url = 'https://youtube.com'#str(input("Enter a website"))
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
images = soup.find_all('img')
counter = 0

if not os.path.exists('./images'):
    os.mkdir('./images')

for img in images:
    if(img['src'][-3:]!= 'gif'):
        path = './images/' + str(counter) + '.jpg'
        with open(path, 'wb') as f:
            if(img['src'][:4] == 'http' or not img['src'][:2] == '//'):
                id = re.search('vi',str(img['src'])).end() + 1
                response = requests.get('https://img.youtube.com/vi/' + img['src'][id:id+11] +  '/maxresdefault.jpg')
            f.write(response.content);
        counter+=1

