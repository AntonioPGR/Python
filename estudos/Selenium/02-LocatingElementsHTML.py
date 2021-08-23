from selenium import webdriver
from selenium.webdriver.common.keys import \
    Keys  # permite que o bot use ações precionando teclas ( pressione enter por ex )
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)
driver.get('https://www.techwithtim.net/')

search = driver.find_element_by_name('s')
search.send_keys('test')
search.send_keys(Keys.RETURN)

try:
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'main'))
    )
    # o driver espera no maximo 10 segundos até que encontre o elemento com id 'contents', isso evita que ele busque enquanto a pagina carrega e retorne um erro
    artigos = results.find_elements(By.TAG_NAME, 'article')
    for artigo in artigos:
        titulo = artigo.find_element(By.CLASS_NAME, 'entry-summary')
        print(titulo.text)
finally:
    driver.quit()  # --> fecha o navegador inteiro

# driver.page_source --> código da pagina