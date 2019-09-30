import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/feed/trending'#str(input("Enter a website"))

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

images = soup.find_all('img')

for img in images:
    print(img['src'])
    if(img['src'][-3:]):
        print()
    