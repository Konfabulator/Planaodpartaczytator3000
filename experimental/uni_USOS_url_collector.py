from bs4 import BeautifulSoup
import requests

Unis_urls = []
Unis = []
Uni_short = []

# get everything under title "Current installations"
url = 'https://usosapps.kpu.krosno.pl/developers/api/definitions/installations/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# find Current installations
current_installations = soup.find('h2', text='Current installations')
# get all <li> tags under Current installations
lis = current_installations.find_next('ul').find_all('li')
# get all <a> tags under <li> tags
for li in lis:
    Unis.append(li.find('p').find('b').text)
    url = li.find('a').text.replace('/developers/api/', '/services/courses/course?')
    Unis_urls.append(url)
    Uni_short.append(url.split('.')[1])
for u0,u1,u2 in zip(Uni_short, Unis, Unis_urls):
    print(f'elif uczelnia == \'{u0}\':\t\t#{u1}\n\turl = \'{u2}\'')
    
for u0,u1 in zip(Uni_short, Unis):
    print(f'"{u1}" : \t"{u0}"')