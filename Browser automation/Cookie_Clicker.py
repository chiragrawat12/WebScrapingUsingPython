from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome("chromedriver.exe")
driver.get("https://orteil.dashnet.org/cookieclicker/")
actions=ActionChains(driver)
driver.implicitly_wait(10)
cookie=driver.find_element_by_id("bigCookie")
cookie_count=driver.find_element_by_id("cookies")
items=[driver.find_element_by_id("productPrice"+str(i)) for i in range(1,-1,-1)]
actions.click(cookie)
for x in range(2000):
    actions.perform()
    count=int(cookie_count.text.split(" ")[0])
    for item in items:
        value=int(item.text)
        if value<=count:
            upgrade_actions=ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()

