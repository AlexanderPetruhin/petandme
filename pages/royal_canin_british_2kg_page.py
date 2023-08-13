from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver import ActionChains
import time

class Royal_canin_british_2kg_page(Base):

    url = 'https://petandme.ru/catalog/cats/sukhoy-korm/royal-canin-british-shorthair-adult-sukhoy-sbalansirovannyy-korm-dlya-britanskikh-korotkosherstnykh-_3/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    page_title = "//*[@id='pagetitle']"
    product_title = "//*[@id='bx_117848907_17215']/div[2]/div/div[1]/div[2]"
    vendor_code = "//*[@id='bx_117848907_17215']/div[2]/div/div[1]/div[1]/div[2]/div/span[2]"
    price = "//*[@id='bx_117848907_17215']/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div/span/span[1]/span[1]"
    add_to_cart_button = "//*[@id='bx_117848907_17215_basket_actions']/span"
    cart_button = "//*[@id='header']/div[2]/div[1]/div/div/div/div[3]/span[3]/a/span/i"









    #Getters

    def get_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.page_title)))

    def get_product_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_title)))

    def get_vendor_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.vendor_code)))

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))













    #Actions

    """Проверяем заголовок страницы выбранного товара"""
    def check_page_title(self):
        self.assert_word(self.get_page_title(), "Royal Canin British Shorthair Adult-сухой сбалансированный корм для британских короткошерстных кошек 2 кг")

    """Проверяем название выбранного товара"""
    def check_product_title(self):
        self.assert_word(self.get_product_title(), "Royal Canin British Shorthair Adult-сухой сбалансированный корм для британских короткошерстных кошек")

    """Проверяем артикул выбранного товара"""
    def check_vendor_code(self):
        self.assert_word(self.get_vendor_code(), "25570200")

    """Проверяем цену товара"""
    def check_price(self):
        self.assert_word(self.get_price(), "2 600")

    """Добавляем товар в корзину"""
    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Click Add to cart")

    """Переходим в корзину"""
    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click Cart Button")









    #Methods

    def check_and_add_to_cart_product(self):
        self.get_current_url()
        self.assert_url("https://petandme.ru/catalog/cats/sukhoy-korm/royal-canin-british-shorthair-adult-sukhoy-sbalansirovannyy-korm-dlya-britanskikh-korotkosherstnykh-_3/")
        self.check_page_title()
        self.check_product_title()
        self.check_vendor_code()
        self.check_price()
        self.click_add_to_cart_button()
        time.sleep(2)
        self.click_cart_button()





