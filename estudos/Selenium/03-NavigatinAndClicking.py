from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal')
driver.find_element(By.LINK_TEXT, 'Conteúdo destacado').click()

try:
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Páginas afluentes'))
    )
    results.click()

    results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Ajuda:Erros comuns'))
    )
    results.click()

    driver.forward() # come back to the firts page
    # driver.back() come back one page ago

    sleep(5)
    driver.quit()

except:
    driver.quit()
