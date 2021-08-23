from selenium import webdriver
from selenium.webdriver.common.keys import \
    Keys  # permite que o bot use ações precionando teclas ( pressione enter por ex )
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://globoesporte.globo.com/busca/?q=corinthians')

try:
    resultados = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/ul'))
    )
    noticia = resultados.find_elements(By.TAG_NAME, 'li')
    for artigo in noticia:
        c = 0
        try:
            text = artigo.find_element(By.XPATH, f'//*[@id="content"]/div/div/ul/li[{c}]/div[3]')
            print(text.text)
        except:
            print('error')
        finally:
            c += 1
finally:
    driver.quit()