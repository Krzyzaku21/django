from bs4 import BeautifulSoup as BSoup
import cssutils
selectors = {}
with open('C:/Users/Krzyz/Desktop/Radek Python/Django_Folder/django/css_function/variables/varaibles.html') as webpage:
    html = webpage.read()
    soup = BSoup(html, 'html.parser')
for styles in soup.select('style'):
    css = cssutils.parseString(styles.encode_contents())
    for rule in css:
        if rule.type == rule.STYLE_RULE:
            style = rule.selectorText
            selectors[style] = {}
            for item in rule.style:
                propertyname = item.name
                value = item.value
                selectors[style][propertyname] = value