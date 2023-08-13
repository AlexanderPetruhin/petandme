from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver import ActionChains
import time

class Checkout_page(Base):

    url = 'https://petandme.ru/order/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    page_title = "//*[@id='pagetitle']"
    final_price = "//*[@id='bx-soa-total']/div[2]/div[5]/span[2]"
    order_weight = "//*[@id='bx-soa-total']/div[2]/div[3]/span[2]"
    email = "//*[@id='soa-property-2']"
    delivery_address = "//*[@id='soa-property-7']"
    comments = "//*[@id='orderDescription']"
    accept_checkbox = "#bx-soa-order > div.col-sm-9.bx-soa > div.form > div > div > label.license"










    #Getters

    def get_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.page_title)))


    def get_final_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.final_price)))

    def get_order_weight(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_weight)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_delivery_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_address)))

    def get_comments(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.comments)))

    def get_accept_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.accept_checkbox)))













    #Actions

    """Проверяем заголовок страницы оформления заказа"""
    def check_page_title(self):
        self.assert_word(self.get_page_title(), "Оформление заказа")

    """Проверяем итоговую стоимость товара"""
    def check_final_price(self):
        self.assert_word(self.get_final_price(), "2 600 ₽")

    """Проверяем итоговый общий вес товара"""
    def check_order_weight(self):
        self.assert_word(self.get_order_weight(), "2 кг")

    """Вводим электронную почту"""
    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input Email")

    """Вводим адрес доставки"""
    def input_delivery_address(self, delivery_address):
        self.get_delivery_address().click()
        self.get_delivery_address().send_keys(delivery_address)
        print("Input Delivery Address")

    """Вводим комментарий к заказу"""
    def input_comments(self, comments):
        self.get_comments().click()
        self.get_comments().send_keys(comments)
        print("Input Comments")

    """Нажимаем чек бокс политики конфиденциальности, открываем страницу политики конфиденциальности"""
    def click_accept_checkbox(self):
        actions = ActionChains(self.driver)
        target = self.driver.find_element(By.CSS_SELECTOR, "#bx-soa-order > div.col-sm-9.bx-soa > div.form > div > div > label.license")
        actions.move_to_element(target)
        actions.perform()
        self.get_accept_checkbox().click()
        print("Click Accept Checkbox")












    #Methods

    def finish_order(self):
        self.get_current_url()
        self.assert_url("https://petandme.ru/order/")
        self.check_page_title()
        self.check_final_price()
        self.check_order_weight()
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.input_email("apae@ya.ru")
        self.input_delivery_address("ул. Сергея Лазо 1-3, кв. 40, индекс 347924")
        self.input_comments("Тестирование прошло успешно!")
        time.sleep(2)
        # self.driver.execute_script("window.scrollTo(0, 200)")
        self.click_accept_checkbox()
        time.sleep(2)









