#!python3

import requests
import os
from bs4 import BeautifulSoup

RESULTFOLDER = "out"

def printLogo():
    print('''
 ____  _      _                   _ _             _
|  _ \(_) ___| |__   __ _ _ __ __| | |_ ___  __ _| |_   _
| |_) | |/ __| '_ \ / _` | '__/ _` | __/ _ \/ _` | | | | |
|  _ <| | (__| | | | (_| | | | (_| | ||  __/ (_| | | |_| |
|_| \_\_|\___|_| |_|\__,_|_|  \__,_|\__\___|\__,_|_|\__, |
                                                    |___/
            ''')

def cutUntilSlash(s: str) -> str:
  res = ""
  for i in range(len(s)-1,0,-1):
    if s[i] == "/":
      break
    else:
      res = s[i] + res

  return res

def parseURL(url: str):
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    res = []
    for imgtag in soup.find_all("img", class_="media-wrapper"):
      print("https:" + imgtag["src"])
      res.append("https:" + imgtag["src"])
    return res


def main():
    printLogo()

    while True:
        print("URL? > ", end="")
        url = input()
        images = parseURL(url)

        if len(images) == 0:
          print("ERROR: any images not found")
        else:
          os.makedirs(RESULTFOLDER+"/"+cutUntilSlash(url))
          for image in images:
            response = requests.get(image).content
            with open(RESULTFOLDER+"/"+cutUntilSlash(url)+"/"+cutUntilSlash(image)+".png", "wb") as f:
              f.write(response)


if __name__ == "__main__":
    main()