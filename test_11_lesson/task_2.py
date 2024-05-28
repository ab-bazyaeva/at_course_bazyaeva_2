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

try:
    driver.get(fix_site)
    sleep(2)

# Авторизация на сайте
    login = driver.find_element(By.CSS_SELECTOR, '[class="controls-Field js-controls-Field controls-InputBase__nativeField controls-InputBase__nativeField_caretFilled controls-InputBase__nativeField_caretFilled_theme_default controls-InputBase__nativeField_hideCustomPlaceholder"]')
    login.send_keys('discus_admin1', Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, '[class="controls-Field js-controls-Field controls-InputBase__nativeField controls-Password__nativeField_caretFilled controls-Password__nativeField_caretFilled_theme_default controls-InputBase__nativeField_hideCustomPlaceholder"]')
    password.send_keys("discus_admin12", Keys.ENTER)
    # driver.find_element(By.ID, '["class="auth-AdaptiveLoginForm__loginButtonImage controls-BaseButton__icon controls-icon controls-icon_size-m controls-icon_style-contrast"]').click()
    sleep(7)

# Переход в реестр "Контакты"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Контакты']"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="NavigationPanels-SubMenu__headTitle   NavigationPanels-SubMenu__title-with-separator NavigationPanels-Accordion__prevent-default"]'))).click()

# Открытие панели выбора пользователя
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="controls-BaseButton__icon controls-icon_size-m controls-icon icon-RoundPlus"]'))).click()
    sleep(4)
# Поиск пользователя
    input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[name="ws-input_2024-05-28"]')))
    input_field.send_keys("Админинсайд Обсуждения")
    sleep(2)

# Клик на найденного пользователя
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[title="Админинсайд Обсуждения"]'))).click()
    sleep(2)

# Ввод текста
    message_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="textEditor_Viewer__Paragraph textEditor_Viewer__Paragraph_empty"]')))
    message_input.send_keys("Давайте делать просто тишину, \nМы слишком любим собственные речи,\nИ из-за них не слышно никому\nСвоих друзей на самой близкой встрече, \nДавайте делать просто тишину.", Keys.ENTER)
    sleep(3)

# Проверка, что сообщение появилось в реестре
    massage_new = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="msg-dialogs-item__content-inner msg-entity-content__inner ws-flex-shrink-1 ws-flex-grow-1"]')))

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
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.XPATH, "//span[text()='Давайте делать просто тишину,']")))

# Завершение работы драйвера
finally:
    driver.quit()