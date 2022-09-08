from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path_selenium = ("../chromedriver.exe")
driver = webdriver.Chrome(path_selenium)

driver.get("https://github.com/JoseMateusCamargo")
print(driver.title)

''' 2 example :) 
driver.get("https://www.google.com")
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("python")
search_bar.send_keys(Keys.RETURN)
'''

print(driver.current_url)
driver.save_screenshot(str(driver.title) + '.png')
print('Save as: %s' % str(driver.title) + '.png')
driver.close()
