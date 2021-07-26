import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    url = requests.get("https://en.wikipedia.org/wiki/Special:random")
    soup = BeautifulSoup(url.content, 'html.parser')
    title = soup.find(id="firstHeading").string
    view = input(title + "\n Do you want to view this article? y/n: ")
    if view.lower() == "y":
        url = "https://en.wikipedia.org/wiki/" + title
        webbrowser.open(url)
        break
    elif view.lower() == "n":
        continue
    else:
        print("This input is unaccepted")
        break

