from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Form:


   def __init__(self, url="https://www.imdb.com/search/name/"):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       # Explicit wait
       self.wait = WebDriverWait(self.driver, 10)


   def boot(self):
       self.driver.get(self.url)
       self.driver.maximize_window()
       self.wait.until(ec.url_to_be(self.url))


   def quit(self):
       self.driver.quit()

   def findElementByID(self, id):
       return self.driver.find_element(by=By.ID, value=id)

   def findElementByLINK_TEXT(self, value):
       return self.driver.find_element(by=By.TAG_NAME, value=value)


   def fillForm(self):

       self.wait.until(ec.presence_of_element_located((By.TAG_NAME, "button"))).click()
       self.wait.until(ec.presence_of_element_located((By.ID, "text-input__9"))).send_keys("nivi")
       self.wait.until(ec.presence_of_element_located((By.ID, "text-input__24"))).send_keys("vijai")
       self.wait.until(ec.presence_of_element_located((By.ID, "text-input__10"))).send_keys("ABC")
       self.wait.until(ec.presence_of_element_located((By.ID, "text-input__41"))).send_keys("123")
       self.wait.until(ec.presence_of_element_located((By.ID, "text-input__16"))).send_keys("123")

       self.quit()





form = Form("https://www.imdb.com/search/name/")
form.fillForm()
form.quit()
