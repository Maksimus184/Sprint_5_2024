import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import personal_account, email_from_personal_account, password_from_personal_account, go_button_from_personal_account
from config import emails, passwords

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Выполняем вход с главной страницы Личный кабинет
driver.find_element(By.XPATH, personal_account).click()
driver.find_element(By.XPATH, email_from_personal_account ).send_keys(emails)
time.sleep(3)
driver.find_element(By.XPATH, password_from_personal_account ).send_keys(passwords)
driver.find_element(By.XPATH, go_button_from_personal_account).click()
time.sleep(10)

print("Вход выполнен успешно!")
driver.quit()
