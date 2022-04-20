import keyboard
from concurrent import futures
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import asyncio
from waiting import wait

thread1 = 0
thread2 = 0
yandex = 'yandexdriver.exe'
chrome = 'chromedriver.exe'
firefox = 'geckodriver.exe'

link_b = 'https://www.binance.com/ru/nft/goods/detail?productId='
link_a = '&isProduct=1'

#assets = [45161845, 45161843]
#47129861 test
assets = [46144761]
search = False
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--start-maximized")

pressed = False

def runSearching(asset):
			driver = webdriver.Chrome(service=Service(yandex),options = chrome_options)
			link = link_b + str(asset) + link_a
			driver.get(link)
			wait(lambda :keyboard.read_key() == '0',timeout_seconds = 1200000 )

			el = WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1gv20g8')))
			driver.find_element(By.CLASS_NAME, 'css-1gv20g8').click()
			el2 = WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1p9f32f')))
			driver.find_element(By.CLASS_NAME, 'css-1p9f32f').click()

			wait(lambda :keyboard.read_key() == '0',timeout_seconds = 1200000 )
			#css-19v461i test
			#css-1p9f32f real

if __name__ == '__main__':
			with futures.ThreadPoolExecutor() as executor:
						tests = [executor.submit(runSearching, i) for i in assets]
						a = executor.submit(wait)
						a.result()
						for test in tests:
									try:
												result = test.result()  # can use `timeout` to wait max seconds for each thread
									except Exception as exc:  # can give a exception in some thread, but
												print(exc)