# ? cd C:\Users\Krzyz\Desktop\Radek Python\Django_Folder\virtual_django_venv\Scripts\
# ? activate
#todo leave virtual django venv - (virtual_django_venv)
# ? deactivate
#run with virtual_django_venv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.close()
