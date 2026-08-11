from selenium import webdriver
import time

print("Selenium imported successfully!")

driver = webdriver.Chrome()

print("Chrome opened successfully!")

driver.get("https://www.google.com")

driver.maximize_window()

time.sleep(5)

driver.quit()

print("Chrome closed successfully!")