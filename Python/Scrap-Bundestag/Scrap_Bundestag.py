# Scrap Bundestag allows to get information about each member of Bundestag amd links to their social networks.
# Project goal is to get familiar with parcing though libraries "Requests", "beautifulsoup4", "lxml"
# Deutscher Bundestag website is used as a source of information - https://www.bundestag.de/en/members

from unicodedata import name
from unittest import result
import requests
from bs4 import BeautifulSoup
import json

# Create empty dictionary
persons_url_list = []

# Get list of memebers. Number 740 was obtained via work with get-request obtained from "Inspect element"
# https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset=737
# 737 is the latest available number in the list
for i in range (0, 740, 20):
    url = f'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}'
    
    # Generate get-query and collect all links with members
    q = requests.get(url)
    result = q.content
    
    # Create an object of BeautifulSoup
    soup = BeautifulSoup(result, 'lxml')
    
    # Link to each card in availble in the class "bt-open-in-overlay"
    persons = soup.find_all(class_='bt-open-in-overlay')
    
    # Get list of people
    for person in persons:
        person_page_url = person.get('href')
        persons_url_list.append(person_page_url)

# Save list of members in a dedicated file
with open('persons_url_list.txt', 'a') as file:
    for line in persons_url_list:
        file.write(f'{line}\n')

# Open recently generated file
with open('persons_url_list.txt') as file:
    lines = [line.strip() for line in file.readlines()]

    # Create empty dictionary for all people
    data_dict = []

    for line in lines:
        q = requests.get(line)
        result = q.content

        # Get person name and company
        soup = BeautifulSoup(result, 'lxml')
        person = soup.find(class_='bt-biografie-name').find('h3').text
        person_name_company = person.strip().split(',')
        person_name = person_name_company[0]
        person_company = person_name_company[1].strip()

        # Get links to social networks
        social_networks = soup.find_all(class_='bt-link-extern')

        social_networks_urls = []
        for item in social_networks:
            social_networks_urls.append(item.get('href'))

        data = {
            'person_name': person_name,
            'company_name': person_company,
            'social_networks': social_networks_urls
        }

        # Add element to the dictionary on each iteration
        data_dict.append(data)

        # Create output json-file
        with open('data.json', 'w') as json_file:
            json.dump(data_dict, json_file, indent=4)

