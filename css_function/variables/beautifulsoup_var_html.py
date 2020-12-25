from bs4 import BeautifulSoup
import requests
with open('C:/Users/Krzyz/Desktop/Radek Python/Django_Folder/django/css_function/variables/varaibles.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

match = soup.title.text
print(match)

match2 = soup.find('div', class_='two')
print(match2)

light_theme_btn = soup.find('button', id='light-theme-btn')
print(light_theme_btn)

link = soup.find('div', class_='link')
link_text = link.h1.a.text
print(link_text)

# for item_child in soup.select("div.one"):
#     print(item_child.get_text())