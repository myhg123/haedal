import bs4
import requests
import csv

headers ={
    'User-Agent': 'Not_Crawling X'
}

response = requests.get('https://kin.naver.com/').text
soup = bs4.BeautifulSoup(response, 'html.parser')
ranks = soup.select('#rankingChart > ul > li')

number = lambda rank: int(rank.select_one('span.no').text)
title = lambda rank: rank.select_one('a.ranking_title').text

with open('지식인 순위.csv','w') as ff:
    writer = csv.writer(ff)
    for rank in sorted(ranks, key=number):
       numbers = number(rank)
       titles = title(rank)
       writer.writerow([f'{numbers}위', titles])




