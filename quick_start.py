from bs4 import BeautifulSoup

# Quick Start
with open("/Users/evansanford/Playground/beautiful_soup_bs/the_dormouses_story.html") as fp:
    soup = BeautifulSoup(fp, 'lxml')
print(soup.prettify())

# Simple ways to navigate the soup data structure
print("TITLE\n", soup.title)
print("TITLE NAME\n", soup.title.name)
print("TITLE PARENT NAME\n", soup.title.parent.name)
print("P ELEM\n", soup.p)
print('P ELEM CLASS VALUE\n', soup.p['class'])
print('A ELEM\n', soup.a)
print("ALL A ELEM's\n", soup.find_all('a'))
print("id = 'link3'\n", soup.find(id='link3'))

# Extracting all URL's found within <a> tags:
for link in soup.find_all('a'):
    print(link.get('href'))

# Exract all text from page:
print(soup.get_text())
