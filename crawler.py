from selenium import webdriver
# path to chromedriver.exe 
path = 'chromedriver.exe'
# create nstance of webdriver
driver = webdriver.Chrome(path)
# google url
url = 'https://www.genealog.cl/Geneanexus/search'
# Code to open a specific url
driver.get(url)
searchbox = driver.find_element_by_name('s')
#searchbox.click()
searchbox.send_keys("VERA NAVARRO, JUAN ANDRÉS")
button = driver.find_element_by_id("searchSubmitInitial")
button.click()
sug_html = driver.find_element_by_class_name('striped results-table').get_attribute('textContent')
print(sug_html)
