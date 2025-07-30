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

# --- Caso de Teste 3: Finali pedido

print("Teste 1: Realizando busca...")
wait = WebDriverWait(driver, 10)
search_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Buscar')]")))
search_input.send_keys("camisa")
search_input.send_keys(Keys.ENTER)
time.sleep(3)
assert "camisa" in driver.page_source.lower()
print("✅ Busca realizada com sucesso.")


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

print("Teste 3: Continuando para finalizar o pedido...")
continuar_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'bg-primary') and contains(@class, 'w-full') and contains(translate(text(), 'abcdefghijklmnopqrstuvwxyzáàãâéèêíïóôõöúç', 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÃÂÉÈÊÍÏÓÔÕÖÚÇ'), 'CONTINUAR')]"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", continuar_button)
time.sleep(0.3)
continuar_button.click()
print("✅ Clique em CONTINUAR realizado.")


# Aguarda a tela de checkout carregar
print("Teste 4: Preenchendo dados do pedido...")

# Seleciona como deseja receber o pedido (combobox customizado)
receber_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox' and contains(.,'Selecione como deseja receber o pedido') or contains(.,'Selecione')]"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", receber_button)
time.sleep(0.3)
receber_button.click()
# Aguarda e clica na primeira opção disponível (ex: Entrega/Delivery)
primeira_opcao = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@role='option' and not(@aria-disabled='true')][1] | //div[@data-state='open']//div[@role='option' and not(@aria-disabled='true')][1]"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", primeira_opcao)
time.sleep(0.3)
primeira_opcao.click()

# Seleciona forma de pagamento (combobox customizado)
pagamento_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox' and (contains(.,'Selecione a forma de pagamento') or contains(.,'Selecione'))]"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", pagamento_button)
time.sleep(0.3)
pagamento_button.click()
# Aguarda e clica na primeira opção disponível (ex: PIX, Cartão, Dinheiro)
opcao_pagamento = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@role='option' and not(@aria-disabled='true')][1] | //div[@data-state='open']//div[@role='option' and not(@aria-disabled='true')][1]"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", opcao_pagamento)
time.sleep(0.3)
opcao_pagamento.click()

# Preenche número do WhatsApp
whatsapp_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='whatsapp' or contains(@placeholder, 'WhatsApp') or contains(@placeholder, '99999-9999') or contains(@placeholder, '99999') or contains(@placeholder, '9999') ]"))
)
whatsapp_input.clear()
whatsapp_input.send_keys("(85) 99999-9999")

# Preenche nome para contato
nome_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='contactName' or contains(@placeholder, 'nome completo')]"))
)
nome_input.clear()
nome_input.send_keys("João da Silva")

# Seleciona cidade (combobox customizado)
cidade_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox' and (contains(.,'Selecione a cidade') or contains(.,'Selecione'))]"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cidade_button)
time.sleep(0.3)
cidade_button.click()
opcao_cidade = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@role='option' and not(@aria-disabled='true')][1] | //div[@data-state='open']//div[@role='option' and not(@aria-disabled='true')][1]"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", opcao_cidade)
time.sleep(0.3)
opcao_cidade.click()

# Preenche bairro
bairro_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='neighborhood' or contains(@placeholder, 'Centro')]"))
)
bairro_input.clear()
bairro_input.send_keys("Centro")

# Preenche rua/avenida
rua_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='street' or contains(@placeholder, 'Plácido Castelo')]"))
)
rua_input.clear()
rua_input.send_keys("Av. Plácido Castelo")

# Preenche número
numero_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='number']"))
)
numero_input.clear()
numero_input.send_keys("123")

# Preenche complemento
complemento_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='complement' or contains(@placeholder, 'Apto, casa, etc.')]"))
)
complemento_input.clear()
complemento_input.send_keys("Apto 101")

# Preenche ponto de referência
referencia_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='reference' or contains(@placeholder, 'Próximo a')]"))
)
referencia_input.clear()
referencia_input.send_keys("Próximo ao mercado")

# Clica em FAZER PEDIDO
fazer_pedido_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(translate(text(), 'abcdefghijklmnopqrstuvwxyzáàãâéèêíïóôõöúç', 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÃÂÉÈÊÍÏÓÔÕÖÚÇ'), 'FAZER PEDIDO')]"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", fazer_pedido_button)
time.sleep(0.5)
fazer_pedido_button.click()
print("✅ Pedido realizado.")

# Se aparecer modal de loja fechada, clica em 'Finalizar Pedido'
try:
    modal_finalizar = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='dialog']//button[contains(translate(text(), 'abcdefghijklmnopqrstuvwxyzáàãâéèêíïóôõöúç', 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÃÂÉÈÊÍÏÓÔÕÖÚÇ'), 'FINALIZAR PEDIDO')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", modal_finalizar)
    time.sleep(0.3)
    modal_finalizar.click()
    print("✅ Modal de loja fechada tratado e pedido finalizado.")
except Exception:
    print("Nenhum modal de loja fechada detectado.")

# Aguarda 5 segundos antes de finalizar
print("Aguardando antes de finalizar...")
time.sleep(10)

# Finalizar
driver.quit()