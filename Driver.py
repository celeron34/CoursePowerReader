# Python 3.10.7
# selenium 4.10.0
# 2023/07/09

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By as by
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import Select
from time import sleep

class Browser():
	driver = webdriver
	def __init__(self, gui:bool=True, resultPng:bool=False):
		'''selenium 4.10.0'''
		self.resultPng = resultPng
		options = Options()
		if not gui:
			options.add_argument('--headless=new')
		self.driver = webdriver.Chrome(options=options)

	def __enter__(self):
		return self

	def __exit__(self, *args):
		self.driver.quit()

	def __del__(self):
		self.driver.quit()

	def getXPath(self, XPATH:str, countOut:int=10) -> list[WebElement]:
		''' XPath を指定して WebElement を取得'''
		for _ in range(countOut):
			try:
				elements = self.driver.find_elements(by.XPATH, XPATH)
				return elements
			except: sleep(0.5)
		return []

	''' 指定した URL にアクセス'''
	def jumpURL(self, url:str):
		return self.driver.get(url)
	
	''' 指定した XPath または WebElement のテキストを取得 '''
	def getXPathText(self, XPATH:str | WebElement, countOut:int=10) -> list[str]:
		for _ in range(countOut):
			try:
				if type(XPATH) == WebElement: return [XPATH.text]
				elements = self.driver.find_elements(by.XPATH, XPATH)
				if len(elements) == 1:
					return [elements[0].text]
				elif len(elements) == 0:
					return ['']
				else:
					ret = [str]
					for i in range(len(elements)):
						ret.append(elements[i].text)
					return ret
			except: sleep(0.5)
		return ['']

	'''指定した XPath または WebElement をクリック'''
	def clickXPath(self, XPATH:str | WebElement, countOut:int=10) -> bool:
		for _ in range(countOut):
			try:
				if type(XPATH) == WebElement: XPATH.click()
				self.driver.find_element(by.XPATH, XPATH).click()
				return True
			except:
				sleep(0.5)
		return False

	'''指定した XPath または WebElement に入力'''
	def sendXPath(self, XPATH:str | WebElement, key):
		if type(XPATH) == WebElement: return XPATH.send_keys(key)
		self.driver.find_element(by.XPATH, XPATH).send_keys(key)

	''' 指定した XPath のフレームへ移動'''
	def swFrame(self, XPATH:str):
		self.driver.switch_to.frame(self.driver.find_element(by.XPATH, XPATH))

	''' 現在のフレームの親フレームに移動'''
	def parentFrame(self):
		self.driver.switch_to.parent_frame()

	def getXPathAttr(self, XPATH:str, atr:str) -> str | list[str]:
		elements = self.driver.find_elements(by.XPATH, XPATH)
		if len(elements) == 1:
			return elements[0].get_attribute(atr)
		elif len(elements) == 0:
			return ''
		else:
			ret = []
			for i in range(len(elements)):
				ret.append(elements[i].get_attribute(atr))
			return ret

	def refresh(self):
		self.driver.refresh()

	def getSorce(self) -> str:
		return self.driver.page_source

	def getURL(self) -> str:
		return self.driver.current_url

	def screenshot(self, path:str):
		self.driver.save_screenshot(path)

	def selectList(self, XPATH:str, VALUE:str):
		Select(self.driver.find_element(by.XPATH, XPATH)).select_by_value(VALUE)

	def back(self, re:int=1):
		for _ in range(re):
			self.driver.back()
	
	def quit(self):
		if self.resultPng:
			try:
				self.driver.save_screenshot('./result.png')
			except Exception as e:
				print(e)
		self.driver.quit()
		