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
# Preenche o campo de email
email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
email_input.clear()
email_input.send_keys("rivaldo@gmail.com")
time.sleep(1)

# Preenche o campo de senha
password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
password_input.clear()
password_input.send_keys("12345")
time.sleep(1)

# Clica no botão de login
login_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and (contains(.,'Entrar') or contains(.,'Login'))]"))
)
login_button.click()

print("✅ Login realizado.")
time.sleep(5)

