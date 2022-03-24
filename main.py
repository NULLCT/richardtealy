#!python3

import requests
from bs4 import BeautifulSoup


def printLogo():
    print('''
 ____  _      _                   _ _             _
|  _ \(_) ___| |__   __ _ _ __ __| | |_ ___  __ _| |_   _
| |_) | |/ __| '_ \ / _` | '__/ _` | __/ _ \/ _` | | | | |
|  _ <| | (__| | | | (_| | | | (_| | ||  __/ (_| | | |_| |
|_| \_\_|\___|_| |_|\__,_|_|  \__,_|\__\___|\__,_|_|\__, |
                                                    |___/
            ''')


def parseURL(url: str):
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    for imgtag in soup.find_all("img", class_="media-wrapper"):
      print("https:" + imgtag["src"])


def main():
    printLogo()

    while True:
        print("URL? > ", end="")
        url = input()
        parseURL(url)


if __name__ == "__main__":
    main()
