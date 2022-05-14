from selenium import webdriver

driver = webdriver.Chrome()
driver.quit()

'''
options = webdriver.EdgeOptions()
options.use_chromium = True
driver = webdriver.Edge(options=options)
driver = webdriver.Edge()
'''