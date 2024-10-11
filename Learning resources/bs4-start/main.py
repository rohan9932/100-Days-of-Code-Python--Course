from bs4 import BeautifulSoup
import lxml

with open(file="website.html") as website:
    contents = website.read()

soup = BeautifulSoup(contents, "lxml")
print(soup.h1.string)
# print(soup.prettify()) # indents the soup file

all_lists = soup.find_all(name="li")
print(all_lists)

all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading.getText())

section_heading = soup.find(name="h3", class_="heading") # written attribute class_ so that it doesn't clash with "class"
print(section_heading.getText())

# use css selector to find a item
company_link = soup.select_one(selector="p a")
print(company_link.get("href"))

headings = soup.select(selector=".heading")
print(headings)
