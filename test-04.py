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
driver.get("https://vestirme.vercel.app/admin/login")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# -- Realizando login na aplicação
email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
email_input.clear()
email_input.send_keys("rivaldo@gmail.com")
time.sleep(1)

password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
password_input.clear()
password_input.send_keys("12345")
time.sleep(1)

login_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and (contains(.,'Entrar') or contains(.,'Login'))]"))
)
login_button.click()
print("✅ Login realizado.")
time.sleep(2)

# -- Navega para o menu de produtos
produtos_link = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/admin/produtos')]"))
)
produtos_link.click()
print("✅ Navegou para a tela de produtos.")
time.sleep(2)

# -- Cadastro de produto (lógica já existente)
add_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div/div[1]/div[2]/button[2]"))
)
add_button.click()
print("✅ Botão de adicionar produto clicado.")

wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='dialog']")))

nome_input = wait.until(EC.presence_of_element_located((By.NAME, "nome")))
nome_input.clear()
nome_input.send_keys("Camiseta Básica Teste")
time.sleep(1)

descricao_input = driver.find_element(By.NAME, "descricao")
descricao_input.clear()
descricao_input.send_keys("Camiseta confortável para testes automatizados.")
time.sleep(1)

preco_input = driver.find_element(By.NAME, "precoPadrao")
preco_input.clear()
preco_input.send_keys("99,90")
time.sleep(1)

disponivel_switch = driver.find_element(By.ID, "disponivel")
if disponivel_switch.get_attribute("aria-checked") == "false":
    disponivel_switch.click()
time.sleep(1)

destacar_switch = driver.find_element(By.ID, "destacar")
if destacar_switch.get_attribute("aria-checked") == "false":
    destacar_switch.click()
time.sleep(1)

categoria_button = driver.find_element(By.ID, "idCategoria")
categoria_button.click()
time.sleep(0.5)
primeira_categoria = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@role='option' and not(@aria-disabled='true') and not(contains(.,'Nenhuma'))]"))
)
primeira_categoria.click()

salvar_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(.,'Salvar')]"))
)
salvar_button.click()

print("✅ Produto cadastrado com sucesso!")
time.sleep(5)