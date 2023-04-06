# App allows to parse websites and grab information from them
# Beautifulsoup library is used for it
# Link: https://beautiful-soup-4.readthedocs.io/en/latest/

from bs4 import BeautifulSoup
import urllib.request

request = urllib.request.urlopen('https://www.ua-football.com/sport')

# Grab news
soup = BeautifulSoup(request.read(), 'html.parser')
news = soup.find_all('li', class_='liga-news-item')

# Create output dictionary
results = []
for item in news:
    title = item.find('span', class_='d-block').get_text(strip=True)
    desc = item.find('span', class_='name-dop').get_text(strip=True)
    href = item.a.get('href')
    results.append({
        'title': title,
        'desc': desc,
        'href': href,
    })

# Save output in TXT file
f = open('news.txt', 'w')
i = 1
for item in results:
    f.write(f'News {i}\n\nTitle: {item["title"]}\nDescription: {item["desc"]}\nLink: {item["href"]}\n===============\n')
    i += 1
f.close()