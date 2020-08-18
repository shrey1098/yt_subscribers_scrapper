import pandas as pd
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
import csv

sheet = pd.read_csv('Sheet1.csv')
file = "output.csv"
f = open(file, "w+")
f.close()
for i in (range(len(sheet['Channel_Title']))):
    id = sheet['Channel_ID'][i]
    channel_url = "https://www.youtube.com/channel/%s" % id
    channel_name = sheet['Channel_Title'][i]
    session = HTMLSession()
    response = session.get(channel_url)
    response.html.render(sleep=1, timeout= 100000)
    soup = bs(response.html.html, "html.parser")
    open("video.html", "w", encoding='utf8').write(response.html.html)
    x = soup.find("yt-formatted-string", attrs={"class": "style-scope ytd-c4-tabbed-header-renderer"}).text
    with open('output.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([i, "%s" % channel_name, "%s" % x])
