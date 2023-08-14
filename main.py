from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


#the most expensive usernames may come from noun wordlists downloaded from GitHub, accessed like such:
#with open('filename.txt', 'r') as text_file:   
    #combined_list = text_file.read().split(',')

#but names with short length
letters = [chr(x) for x in range(97, 123)]
numbers = [str(x) for x in range(10)]
combined_list = letters + numbers

#using FireFox driver
driver = webdriver.Firefox()
#different 3rd party API users exist, but Riot doesn't allow most of them
url = "nameslol"
extension = "name-checker"
for e1 in combined_list:
    for e2 in combined_list:
        driver.get("https://www." + url + ".com/" + extension)
        search = driver.find_element(By.CSS_SELECTOR, '[class="focus:ring-primary-500 focus:order-primary-500 shadow-sm-light block w-full rounded-lg border border-gray-600 bg-gray-700 p-2.5 text-sm text-white placeholder-gray-400 shadow-sm"]')
        str = e1 + " " + e2
        search.send_keys(str)
        submit = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
        submit.click()
        try:
            #wait until the element appears
            #if poor connection, it is possible to increment the duration that is being waited at the expense of computation time
            element = WebDriverWait(driver, 1).until(lambda x: x.find_element(By.CSS_SELECTOR, '[class="text-green-500"]'))
            if element.text == "available":
                print(str)
        except:
            continue
driver.quit()