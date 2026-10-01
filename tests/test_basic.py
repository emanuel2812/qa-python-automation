from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_saucedemo():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    assert "inventory" in driver.current_url

    driver.quit()

def test_login_invalid_password():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("senha_errada")

    login_button.click()

    error_message = driver.find_element(
        By.CSS_SELECTOR, "[data-test='error']"
    )

    assert error_message.is_displayed()

    driver.quit()

def test_login_invalid_username():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.send_keys("usuario_invalido")
    password.send_keys("secret_sauce")

    login_button.click()

    error_message = driver.find_element(
        By.CSS_SELECTOR, "[data-test='error']"
    )

    assert error_message.is_displayed()

    driver.quit()   