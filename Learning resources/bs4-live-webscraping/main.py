from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "lxml")

titles = soup.find_all(name="span", class_="titleline")
title_texts = []
title_links = []

for title in titles:
    text = title.getText()
    title_texts.append(text)
    link = title.find(name="a").get("href")
    title_links.append(link)

title_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")] # list comprehension

print(title_texts)
print(title_links)
print(title_upvotes)

# finding the highest upvote
highest_upvote = max(title_upvotes)
# for upvote in title_upvotes:
#     if upvote > highest_upvote:
#         highest_upvote = upvote

# index of the highest upvote
highest_upvote_index = title_upvotes.index(highest_upvote)
highest_upvote_text = title_texts[highest_upvote_index]
highest_upvote_link = title_links[highest_upvote_index]
print(highest_upvote_text)
print(highest_upvote_link)
print(highest_upvote)

