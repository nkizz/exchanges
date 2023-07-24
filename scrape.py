from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
print("starting driver")
driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
print("Started driver, getting initial page")
driver.get('http://tenproject.cloudapp.net/tensearch.aspx')
page = 1
while True:
	src = driver.page_source
	f = open(str(page) + '.html', 'w')
	f.write(src)
	f.close()
	if src.__contains__('Server Error'):
		break
	page += 1
	print("Getting page ", page)
	driver.execute_script("__doPostBack('ExchangesGrid','Page$" + str(page) + "')")

