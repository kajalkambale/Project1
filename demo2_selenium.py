import time

from selenium import webdriver
def first_project():
    driver=webdriver.Chrome()
    driver.get('https://www.google.com')
    Title=driver.title
    print("Title", Title)
    time.sleep(5)
    driver.quit()

first_project()