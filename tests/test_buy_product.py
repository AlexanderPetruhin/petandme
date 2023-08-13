import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from pages.main_page import Main_page
from pages.cats_page import Cats_page
from pages.royal_canin_british_2kg_page import Royal_canin_british_2kg_page
from pages.cart_page import Cart_page
from pages.checkout_page import Checkout_page

def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    print("Start test")
    mp = Main_page(driver)
    mp.authorization()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 400)")
    mp.choose_cats_food()
    cp = Cats_page(driver)
    cp.find_dry_food()
    driver.execute_script("window.scrollTo(0, 600)")
    cp.filters()
    cp.enter_product_page()
    catc = Royal_canin_british_2kg_page(driver)
    catc.check_and_add_to_cart_product()
    cap = Cart_page(driver)
    cap.check_cart_page_and_checkout()
    cop = Checkout_page(driver)
    cop.finish_order()
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    print("Finish test")

