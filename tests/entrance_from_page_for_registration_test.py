import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import personal_account,registration_from_personal_account, email_log_in, password_to_your_account, go_from_registration_page, go_button
from config import emails, passwords

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Выполняем вход со страницы регистрации
driver.find_element(By.XPATH, personal_account).click()
driver.find_element(By.XPATH, registration_from_personal_account).click()
driver.find_element(By.XPATH, go_from_registration_page).click()
driver.find_element(By.XPATH, email_log_in).send_keys(emails)
driver.find_element(By.XPATH, password_to_your_account).send_keys(passwords)
driver.find_element(By.XPATH, go_button).click()
time.sleep(10)

print("Вход выполнен успешно!")
driver.quit()
