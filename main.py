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

# --- Caso de Teste 2: Adicinar um produto ao carrinho
print("Teste 2: Clicando em um produto...")
try:
    product = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//a[contains(@href,'/produto')])[1]"))
    )
    product.click()
    time.sleep(3)
    assert "/produto" in driver.current_url
    print("Redirecionado para página do produto.")
except TimeoutException:
    print("Nenhum produto encontrado para clicar.")

print("Teste 2: Selecionando cor e tamanho...")
# Seleciona o botão de cor com texto 'Azul'
color_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'rounded-md') and normalize-space(text())='Azul']"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", color_button)
time.sleep(0.5)
color_button.click()

tamanhos = ['P', 'M', 'PP']
size_button = None
for tamanho in tamanhos:
    try:
        size_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[contains(@class, 'rounded-md') and normalize-space(text())='{tamanho}']"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", size_button)
        time.sleep(0.3)
        size_button.click()
        print(f"Selecionado tamanho: {tamanho}")
        break
    except:
        continue
if not size_button:
    print("Nenhum tamanho disponível para selecionar.")

print("Teste 2: Adicionando ao carrinho...")
time.sleep(1)  # Aguarda renderização do botão
add_to_cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'bg-primary') and contains(@class, 'w-full') and contains(translate(text(), 'abcdefghijklmnopqrstuvwxyzáàãâéèêíïóôõöúç', 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÃÂÉÈÊÍÏÓÔÕÖÚÇ'), 'ADICIONAR AO CARRINHO')]"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_button)
time.sleep(0.3)
add_to_cart_button.click()
print("✅ Item adicionado ao carrinho.")

# Aguarda 5 segundos antes de finalizar
print("Aguardando antes de finalizar...")
time.sleep(10)

# Finalizar
driver.quit()
