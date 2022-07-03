import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def get_source_html(url):

    driver = webdriver.Chrome(
        executable_path="C:/OpenServer/domains/___2 pyth/project21_zoon/chromedriver/chromedriver.exe"
    )

    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(3)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_source_html(url='https://samara.zoon.ru/restaurants/')


if __name__ == '__main__':
    main()
