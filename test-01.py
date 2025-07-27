from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://vestirme.vercel.app/demo/home")
driver.maximize_window()
time.sleep(3)

# --- Caso de Teste 1: Realizar uma busca de produto
print("Teste 1: Realizando busca...")
wait = WebDriverWait(driver, 10)
search_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Buscar')]")))
search_input.send_keys("camisa")
search_input.send_keys(Keys.ENTER)
time.sleep(3)
assert "camisa" in driver.page_source.lower()
print("✅ Busca realizada com sucesso.")

# Aguarda 5 segundos antes de finalizar
print("Aguardando antes de finalizar...")
time.sleep(10)

# Finalizar
driver.quit()