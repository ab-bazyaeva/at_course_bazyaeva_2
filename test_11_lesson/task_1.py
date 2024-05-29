# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


service = Service('E:/Рабочая/Программы/Python/chromedriver.exe')
driver = webdriver.Chrome(service=service) # Инициализация драйвера
wait = WebDriverWait(driver,10)
try:
    driver.get("https://sbis.ru/") # Переход на https://sbis.ru/
# Переход в раздел "Контакты"
    contacts_link = wait.until(
    EC.presence_of_element_located((By.LINK_TEXT, "Контакты")))
    contacts_link.click()

# Найти баннер Тензор, кликнуть по нему
    tensor_banner = wait.until(
    EC.presence_of_element_located((By.XPATH, '//img[@alt="Разработчик системы СБИС — компания «Тензор»"]')))
    sleep(2)
    tensor_banner.click()

# Переход на https://tensor.ru/
    driver.switch_to.window(driver.window_handles[1])

# Проверить, что есть блок новости "Сила в людях"
    news_block = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//p[contains(text(), "Сила в людях")]')))
    sleep(2)

# скролл
    driver.execute_script("arguments[0].scrollIntoView();", news_block)
    sleep(2)

# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
    tensor_link = wait.until(
    EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Подробнее")]')))
    tensor_link.click()
    sleep(2)
    wait.until(EC.url_contains("tensor.ru/about"))
    assert 'https://tensor.ru/about/' in driver.current_url


# Завершение работы драйвера
finally:
    driver.quit()
