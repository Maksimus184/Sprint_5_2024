import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
wait = WebDriverWait(driver, 20)

# Определение XPaths для вкладок
tabs = {
    "Булки": "//div[span[text()='Булки']]",
    "Соусы": "//div[span[text()='Соусы']]",
    "Начинки": "//div[span[text()='Начинки']]"
}

try:
    for tab_name, tab_xpath in tabs.items():
        # Ожидание, пока вкладка станет видимой
        tab_element = wait.until(EC.visibility_of_element_located((By.XPATH, tab_xpath)))

        # Прокрутка к элементу
        driver.execute_script("arguments[0].scrollIntoView();", tab_element)

        # Клик по вкладке с использованием JavaScript
        driver.execute_script("arguments[0].click();", tab_element)

        time.sleep(1)  # Задержка для визуализации перехода; лучше использовать ожидания

        # Проверка, что вкладка активна
        active_tab = wait.until(EC.presence_of_element_located((By.XPATH, tab_xpath)))
        assert "tab_tab_type_current__2BEPc" in active_tab.get_attribute("class"), f"Вкладка '{tab_name}' не активна"

        print(f"Тест пройден: переход на вкладку '{tab_name}' выполнен успешно.")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()  # Закрываем драйвер после завершения работы