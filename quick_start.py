from bs4 import BeautifulSoup

# Quick Start
with open("./the_dormouses_story.html") as fp:
    soup = BeautifulSoup(fp, 'lxml')
print(soup.prettify())

print("Simple ways to navigate the soup data structure")

print("soup.title\n", soup.title)
print("soup.title.name\n", soup.title.name)
print("soup.title.parent\n", soup.title.parent.name)
print("soup.p\n", soup.p)
print("soup.p['class']\n", soup.p['class'])
print('soup.a\n', soup.a)
print("soup.find_all('a')\n", soup.find_all('a'))
print("soup.find(id='link3')\n", soup.find(id='link3'))

# Extracting all URL's found within <a> tags:
for link in soup.find_all('a'):
    print(link.get('href'))

# Exract all text from page:
print(soup.get_text())
