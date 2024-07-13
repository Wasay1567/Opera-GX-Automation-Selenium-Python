from selenium import webdriver
from selenium.webdriver.chrome import service
import time
import os
operaPath = "path/to/opera/driver/path"
webdriver_service = service.Service(operaPath)
webdriver_service.start()
options = webdriver.ChromeOptions()
options.binary_location = "path/to/operaGX/browser"
userDir = 'user/data/directory/location'

if not os.path.exists(userDir):
    os.makedirs(userDir)

options.add_experimental_option('w3c', True)
options.add_argument(f"--user-data-dir={userDir}")
# options.add_argument("--incognito")
options.arguments.extend(["--no-default-browser-check", "--no-first-run"])
options.arguments.extend(["--no-sandbox", "--test-type"])
options.add_argument("--start-maximized")
driver = webdriver.Remote(webdriver_service.service_url, options=options)
time.sleep(10)
driver.get("https://twitter.com/")
time.sleep(5)
