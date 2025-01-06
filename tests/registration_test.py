import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import personal_account, registration, name, email, registration_button, password
from config import emails, names, passwords


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Выполняем авторизацию с валидными данными
driver.find_element(By.XPATH, personal_account).click()
driver.find_element(By.XPATH, registration).click()
driver.find_element(By.XPATH, name).send_keys(names)
time.sleep(3)
driver.find_element(By.XPATH, password).click()
wait = WebDriverWait(driver, 3)
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, password)))
password_input.send_keys(passwords)
time.sleep(3)
driver.find_element(By.XPATH, email).click()
wait = WebDriverWait(driver, 3)
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, email)))
password_input.send_keys(emails)
time.sleep(3)
driver.find_element(By.XPATH, email).click()
driver.find_element(By.XPATH, registration_button).click()
time.sleep(10)

print("Тест выполнен успешно!")
driver.quit()

























