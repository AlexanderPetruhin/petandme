from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver import ActionChains
import time

class Cats_page(Base):

    url = 'https://petandme.ru/catalog/cats/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    cats_page_title = "//*[@id='pagetitle']"
    dry_food = "#bx_1847241719_175 > div.img.shine"
    dry_food_title = "//*[@id='pagetitle']"
    slider_left = "//*[@id='left_slider_c4ca4238a0b923820dcc509a6f75849b']"
    slider_right = "//*[@id='right_slider_c4ca4238a0b923820dcc509a6f75849b']"
    brand_button = "#smartfilter > div.bx_filter_parameters > div:nth-child(6) > div.bx_filter_parameters_box_title.icons_fa"
    checkbox_royal_canin = "#smartfilter > div.bx_filter_parameters > div:nth-child(6) > div.bx_filter_block.limited_block > div.bx_filter_parameters_box_container > label:nth-child(2) > span > span"
    weight_button = "#smartfilter > div.bx_filter_parameters > div:nth-child(7) > div.bx_filter_parameters_box_title.icons_fa"
    checkbox_2kg = "#smartfilter > div.bx_filter_parameters > div:nth-child(7) > div.bx_filter_block.limited_block > div.bx_filter_parameters_box_container > div.hidden_values > label:nth-child(10) > span"
    age_button = "#smartfilter > div.bx_filter_parameters > div:nth-child(8) > div.bx_filter_parameters_box_title.icons_fa"
    checkbox_old = "#smartfilter > div.bx_filter_parameters > div:nth-child(8) > div.bx_filter_block.limited_block > div.bx_filter_parameters_box_container > label:nth-child(2) > span > span"
    ingredients_button = "#smartfilter > div.bx_filter_parameters > div:nth-child(9) > div.bx_filter_parameters_box_title.icons_fa"
    checkbox_chicken = "#smartfilter > div.bx_filter_parameters > div:nth-child(9) > div.bx_filter_block.limited_block > div.bx_filter_parameters_box_container > label:nth-child(8) > span > span"
    royal_canin_british = "#bx_3966226736_17215"

    #Getters

    def get_cats_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cats_page_title)))

    def get_dry_food(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.dry_food)))

    def get_dry_food_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dry_food_title)))

    def get_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_left)))

    def get_slider_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_right)))

    def get_brand_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.brand_button)))

    def get_checkbox_royal_canin(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.checkbox_royal_canin)))

    def get_weight_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.weight_button)))

    def get_checkbox_2kg(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.checkbox_2kg)))

    def get_age_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.age_button)))

    def get_checkbox_old(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.checkbox_old)))

    def get_ingredients_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.ingredients_button)))

    def get_checkbox_chicken(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.checkbox_chicken)))

    def get_royal_canin_british(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.royal_canin_british)))












    #Actions

    """Проверяем загловок страницы"""
    def check_cats_title(self):
        self.assert_word(self.get_cats_page_title(), "Кошки")

    """Переходим в раздел 'Сухой корм'"""
    def click_dry_food(self):
        self.get_dry_food().click()
        print("Click Dry Food")


    """Проверяем заголовок страницы сухого корма"""
    def check_dry_food_title(self):
        self.assert_word(self.get_dry_food_title(), "Сухой корм для кошек")


    """Двигаем левый слайдер цены вправо"""
    def move_slider_left(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_slider_left()).move_by_offset(34, 0).release().perform()
        print("Move Price Slider Left")

    """Двигаем правый слайдер цены влево"""
    def move_slider_right(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_slider_right()).move_by_offset(-125, 0).release().perform()
        print("Move Price Slider Right")

    """Открываем фильтр по брендам"""
    def click_brand_button(self):
        self.get_brand_button().click()
        print("Brand Button Click")

    """Ставим галочку в чек боксе Роял Канин"""
    def click_checkbox_royal_canin(self):
        self.get_checkbox_royal_canin().click()
        print("Checkbox Royal Canin Click")

    """Открываем фильтр по весу"""
    def click_weight_button(self):
        self.get_weight_button().click()
        print("Weight Button Click")

    """Ставим галочку в чек боксе 2 кг"""
    def click_checkbox_2kg(self):
        self.get_checkbox_2kg().click()
        print("Checkbox 2KG click")

    """Открываем фильтр по возрасту"""
    def click_age_button(self):
        self.get_age_button().click()
        print("Age button click")

    """Ставим галочку в чек боксе 'Взрослые'"""
    def click_checkbox_old(self):
        self.get_checkbox_old().click()
        print("Checkbox Adults Click")

    """Открываем фильтр по ингредиентам"""
    def click_ingredients_button(self):
        self.get_ingredients_button().click()
        print("Ingredients button click")

    """Ставим галочку в чек боксе - курица"""
    def click_checkbox_chicken(self):
        self.get_checkbox_chicken().click()
        print("Checkbox Chicken Click")

    """Выбираем необходимый товар"""
    def click_royal_canin_british(self):
        self.get_royal_canin_british().click()
        print("Royal Canin British Click")






    #Methods

    def find_dry_food(self):
        self.get_current_url()
        self.assert_url("https://petandme.ru/catalog/cats/")
        self.check_cats_title()
        self.click_dry_food()
        self.check_dry_food_title()
        self.get_current_url()
        self.assert_url("https://petandme.ru/catalog/cats/sukhoy-korm/")

    def filters(self):
        self.move_slider_left()
        self.move_slider_right()
        self.click_brand_button()
        self.click_checkbox_royal_canin()
        time.sleep(2)
        self.click_weight_button()
        self.click_checkbox_2kg()
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.click_age_button()
        self.click_checkbox_old()
        self.click_ingredients_button()
        self.click_checkbox_chicken()
        self.driver.execute_script("window.scrollTo(0, -500)")

    def enter_product_page(self):
        self.click_royal_canin_british()


