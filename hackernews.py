import requests as req
import webbrowser as wb
from bs4 import BeautifulSoup

r = req.get('https://news.ycombinator.com/')

soup = BeautifulSoup(r.text, 'html.parser')

s = soup.find_all(class_ = 'storylink')

dic = {}
for i in range(len(s)):
    dic[i+1] = s[i]['href']
    print(i+1, '.', s[i].text,'\n')

print('PRESS THE NEWS NUMBER TO KNOW THE DETAILED NEWS ON YOUR WEBSITE: \n')
t = int(input())
wb.open(dic[t])


