import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import log_in_to_your_account, email_log_in, password_to_your_account, go_button
from config import emails, passwords

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

wait = WebDriverWait(driver, 20)
# Выполняем вход с главной страницы
wait.until(EC.element_to_be_clickable((By.XPATH, log_in_to_your_account))).click()
time.sleep(1)
wait.until(EC.visibility_of_element_located((By.XPATH, email_log_in))).send_keys(emails)
time.sleep(1)
wait.until(EC.visibility_of_element_located((By.XPATH, password_to_your_account))).send_keys(passwords)
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, go_button))).click()

# Ожидание завершения входа
wait.until(EC.url_changes(driver.current_url))

print("Вход выполнен успешно!")
