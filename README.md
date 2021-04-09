# article-scrapper
This is a python script that takes a filename as argument and scrapes the website 'https://www.theguardian.com/au' for all article that contains the keywords 'corona', 'coronavirus' and 'vaccine' and, saves them in a csv file in the same path with the file name given as argument.

python must be installed in your system to run this script

Install dependencies if not installed already
  pip install requests
  pip install BeautifulSoup4
  
To run from terminal or command line use
  python article_scrapper.py filename
