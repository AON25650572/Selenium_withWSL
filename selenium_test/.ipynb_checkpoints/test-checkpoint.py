from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor="http://192.168.0.2:4444/wd/hub",
    options=chrome_options
    )
driver.get("https://www.google.com/search?q=qiita")
