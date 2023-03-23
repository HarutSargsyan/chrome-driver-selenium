from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driverPath = '/usr/local/bin/chromedriver'
service = Service(driverPath)
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser" # Path to Brave Browser (this is the default)

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://google.com")
print(driver.title)
driver.close()