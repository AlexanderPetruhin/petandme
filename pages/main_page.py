from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver import ActionChains


class Main_page(Base):

    url = 'https://petandme.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    enter_button = "//*[@id='header']/div[1]/div/div/div[2]/div/div/a/span"
    cats_button = "#bx_631207241_127 > div.img.shine > a > img"



    #Authorization modal locators

    login_input = "#USER_LOGIN_POPUP"
    password_input = "#USER_PASSWORD_POPUP"
    login_button = "//*[@id='avtorization-form']/div[3]/div[2]/input"




    #Getters

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_login_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.login_input)))

    def get_password_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.password_input)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_cats_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.cats_button)))







    #Actions

    """Нажимаем кнопку 'Войти'"""
    def click_enter_button(self):
        self.get_enter_button().click()
        print("Click Enter Button")

    """Вводим логин зарегистрированного пользователя в модальном окне"""

    def input_login(self, login_input):
        self.get_login_input().send_keys(login_input)
        print("Input Login")


    """Вводим пароль зарегистрированного пользователя в модальном окне"""
    def input_password(self, password_input):
        self.get_password_input().click()
        self.get_password_input().send_keys(password_input)
        print("Input Password")


    """Нажимаем 'Войти' в модальном окне"""
    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login button")


    """Переходим в раздел 'Кошки'"""
    def click_cats_button(self):
        self.get_cats_button().click()
        print("Click Cats button")



    #Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_enter_button()
        self.input_login("apae@ya.ru")
        self.input_password("aall718254exx")
        self.click_login_button()

    def choose_cats_food(self):
        self.click_cats_button()
