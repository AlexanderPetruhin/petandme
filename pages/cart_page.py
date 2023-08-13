from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver import ActionChains
import time

class Cart_page(Base):

    url = 'https://petandme.ru/basket/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    page_title = "//*[@id='pagetitle']"
    product_title_in_cart = "basket-item-info-name-link"
    price_in_cart = "basket-item-price-current-value"
    final_price = "//*[@id='basket-root']/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div/div[2]"
    checkout_button = "//*[@id='basket-root']/div[2]/div[2]/div/div/div/div/div[2]/div[2]/button"










    #Getters

    def get_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.page_title)))

    def get_product_title_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.product_title_in_cart)))

    def get_price_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.price_in_cart)))

    def get_final_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.final_price)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))












    #Actions

    """Проверяем заголовок страницы - корзина"""
    def check_page_title(self):
        self.assert_word(self.get_page_title(), "Корзина")

    """Проверяем название добавленного в корзину товара"""
    def check_product_title_in_cart(self):
        self.assert_word(self.get_product_title_in_cart(), "Royal Canin British Shorthair Adult-сухой сбалансированный корм для британских короткошерстных кошек")

    """Проверяем цену добавленного в корзину товара"""
    def check_price_in_cart(self):
        self.assert_word(self.get_price_in_cart(), "2 600 ₽")

    """Проверяем итоговую стоимость добавленного товара в корзину"""
    def check_final_price(self):
        self.assert_word(self.get_final_price(), "2 600 ₽")

    """Переходим к оформлению заказа"""
    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")











    #Methods

    def check_cart_page_and_checkout(self):
        self.get_current_url()
        self.assert_url("https://petandme.ru/basket/")
        self.check_page_title()
        self.check_product_title_in_cart()
        self.check_price_in_cart()
        self.check_final_price()
        self.click_checkout_button()








