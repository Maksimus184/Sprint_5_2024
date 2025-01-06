import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import personal_account, registration, name, email, registration_button, password, email_log_in, password_to_your_account, go_button
from config import emails, names, passwords

# Инициализация драйвера
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Ожидание
wait = WebDriverWait(driver, 10)

# Выполняем регистрацию с валидными данными и заходим в личный кабинет
wait.until(EC.element_to_be_clickable((By.XPATH, personal_account))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, registration))).click()

wait.until(EC.visibility_of_element_located((By.XPATH, name))).send_keys(names)
wait.until(EC.element_to_be_clickable((By.XPATH, password))).send_keys(passwords)
wait.until(EC.element_to_be_clickable((By.XPATH, email))).send_keys(emails)
wait.until(EC.element_to_be_clickable((By.XPATH, registration_button))).click()
# Ожидание, пока пользователь не будет перенаправлен на личный кабинет
wait.until(EC.element_to_be_clickable((By.XPATH, personal_account))).click()
# Вход в личный кабинет
wait.until(EC.visibility_of_element_located((By.XPATH, email_log_in))).send_keys(emails)
wait.until(EC.visibility_of_element_located((By.XPATH, password_to_your_account))).send_keys(passwords)
wait.until(EC.element_to_be_clickable((By.XPATH, go_button))).click()
time.sleep(5)
# Ожидание завершения входа
wait.until(EC.element_to_be_clickable((By.XPATH, personal_account))).click()

print("Тест выполнен успешно!")
driver.quit()