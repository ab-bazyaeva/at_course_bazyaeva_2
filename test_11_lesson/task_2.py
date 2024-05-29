# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

service = Service('E:/Рабочая/Программы/Python/chromedriver.exe')
fix_site = 'https://fix-sso.sbis.ru/'
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver,10)

try:
    driver.get(fix_site)
    sleep(2)

# Авторизация на сайте
    login = driver.find_element(By.CSS_SELECTOR,'.controls-Render__field [type="text"]')
    login.send_keys('discus_admin1', Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, '.controls-Render__field [type="password"]')
    password.send_keys("discus_admin12", Keys.ENTER)
    sleep(5)

# Переход в реестр "Контакты"
    element_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Контакты']")))
    actions = ActionChains(driver)
    actions.double_click(element_menu).perform()
    sleep(2)

# Открытие панели выбора пользователя
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]'))).click()
    sleep(3)

# Поиск пользователя
    input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.controls-Render__field [inputmode="text"]')))
    input_field.send_keys("Админинсайд Обсуждения")
    sleep(2)

# Клик на найденного пользователя
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[title="Админинсайд Обсуждения"]'))).click()
    sleep(2)

# Ввод текста
    message_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')))
    message_input.send_keys("Давайте делать просто тишину", Keys.ENTER)
    sleep(2)

# Проверка, что сообщение появилось в реестре
    massage_new = wait.until(EC.presence_of_element_located((By.XPATH, "//p[text()='Давайте делать просто тишину']")))

# Вызов контекстного меню
    action_chains = ActionChains(driver)
    action_chains.move_to_element(massage_new)
    action_chains.context_click(massage_new)
    action_chains.perform()

# Удаление сообщения
    delete_massage = driver.find_element(By.CSS_SELECTOR, '[title="Перенести в удаленные"]')
    delete_massage.click()
    sleep(2)

# Проверка, что сообщение удалено
    wait.until_not(EC.presence_of_element_located((By.XPATH, "//span[text()='Давайте делать просто тишину']")))

# Завершение работы драйвера
finally:
    driver.quit()