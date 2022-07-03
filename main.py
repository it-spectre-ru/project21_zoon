import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


def get_source_html(url):

	driver = webdriver.Chrome(
		executable_path="C:/OpenServer/domains/___2 pyth/project21_zoon/chromedriver/chromedriver.exe"
	)

	driver.maximize_window()

	try:
		driver.get(url=url)
		time.sleep(3)

		while True:
			find_more_element = driver.find_element_by_class_name("catalog-button-showMore")

			if driver.find_elements_by_class_name("hasmore-text"):
				with open("source_page.html", "w") as file:
					file.write(driver.page_source)
				
				break
			else:
				actions = ActionChains(driver)
				actions.move_to_element(find_more_element).perform()
				time.sleep(3)

	except Exception as ex:
		print(ex)
	finally:
		driver.close()
		driver.quit()


def main():
	get_source_html(url='https://orenburg.zoon.ru/restaurants/type/kofejni/')


if __name__ == '__main__':
	main()
