import bs4
import requests

headers ={
    'user-Agent': 'not_crawling X)'
}

response = requests.get('https://kin.naver.com/',headers=headers).text
soup = bs4.BeautifulSoup(response, 'html.parser')

rank = soup.select('#rankingChart > ul > li')

with open('ranking.csv', 'w') as f:
    for ranks in rank:
        number = ranks.select_one('span.no').text
        title = ranks.select_one('a.ranking_title')
        f.write(f'{number},{title}\n')






