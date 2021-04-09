"""
This is a python script that takes a filename as argument and scrapes the website 'https://www.theguardian.com/au'
for all article that contains the keywords 'corona', 'coronavirus' and 'vaccine'
and, saves them in a csv file in the same path with the
file name given as argument.

python must be installed in your system to run this script

Install dependencies if not installed already
pip install requests
pip install BeautifulSoup4

To run from terminal or command line use
python article_scrapper.py filename
"""

import sys
import requests
from bs4 import BeautifulSoup
import csv

if __name__ == "__main__":
    page = requests.get('https://www.theguardian.com/au')  # load the webpage
    soup = BeautifulSoup(page.content, 'html.parser')  # separate the page contents along with their html tag

    # separate all contents with html tag 'a' and attribute 'data-link-name' ='article'
    articles = soup.find_all('a', {"data-link-name": "article"})

    article_links = []
    for article in articles:
        if article.get_text().lower().find('corona') != -1 or article.get_text().lower().find(
                'vaccine') != -1:  # separate all articles containing the keywords mentioned above
            article_links.append(article['href'])

    article_links_unique = set(article_links)  # keep only unique links

    if len(sys.argv) > 1:
        filename = sys.argv[1] + '.csv'
    else:
        raise Exception("Filename not given as argument")

    fields = ['headline', 'article link', 'author name', 'date']

    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        for link in article_links_unique:
            article_page = requests.get(link)  # load the link of the article
            # separate the page contents along with their html tag
            soup = BeautifulSoup(article_page.content, 'html.parser')
            article_head = soup.find('h1')  # find the headline
            article_author = soup.find('address', {"aria-label": "Contributor info"})  # find the author name
            article_date = soup.find('label', {"for": "dateToggle"})  # find the article date
            if article_head is None or article_author is None or article_date is None:
                continue
            # write to csv file
            csvwriter.writerow([article_head.get_text(), link, article_author.get_text().split('@')[0], article_date.get_text()])
