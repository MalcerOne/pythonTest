import requests
import json
from bs4 import BeautifulSoup
import os

# Get the data from the website
def get_data(url):
    r = requests.get(url)
    return r.text

def main():
    category = input("[+] Enter the category: ")
    url = ""

if __name__ == '__main__':
    main()