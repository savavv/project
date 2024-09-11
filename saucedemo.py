from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.saucedemo.com"

browser = webdriver.Chrome()


try:

    browser.get(url)
    time.sleep(2)

    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    time.sleep(2)

    browser.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']").click()
    browser.find_element(By.XPATH, "//button[text()='Add to cart']").click()

    browser.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    assert "Sauce Labs Backpack" in browser.page_source
    time.sleep(2)

    browser.find_element(By.XPATH, "//button[text()='Checkout']").click()
    browser.find_element(By.ID, "first-name").send_keys("User")
    browser.find_element(By.ID, "last-name").send_keys("User_ln")
    browser.find_element(By.ID, "postal-code").send_keys("123456")
    time.sleep(2)
    browser.find_element(By.XPATH, "//input[@type='submit']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//button[text()='Finish']").click()
    time.sleep(2)


    assert "Thank you for your order!" in browser.page_source

finally:

    browser.quit()
