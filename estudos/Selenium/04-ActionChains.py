from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.maximize_window()

driver.get('https://orteil.dashnet.org/cookieclicker/')

driver.implicitly_wait(10)


driver.find_element(By.LINK_TEXT, 'Got it!')

cookie = driver.find_element(By.ID, 'bigCookie')
num_cookie = driver.find_element(By.ID, 'cookies')
items = [driver.find_element(By.ID, 'productPrice'+str(i)) for i in range(1, -1, -1)]

click_actions = ActionChains(driver)
click_actions.click(cookie)

for i in range(10000):
    click_actions.perform()
    my_cookies = int(num_cookie.text.split(' ')[0])
    for item in items:
        item_price = int(item.text)
        if item_price <= my_cookies:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click(item)
            upgrade_actions.perform()