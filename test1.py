from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

import unittest

class Test_FireFox(unittest.TestCase):

	driver = webdriver.Firefox();

	def test_google_search(self):
		# Create a new instance of the Firefox self.driver
		#self.driver = webself.driver.Firefox()

		# go to the google home page
		self.driver.get("http://www.google.com")

		# find the element that's name attribute is q (the google search box)
		inputElement = self.driver.find_element_by_name("q")

		# type in the search
		inputElement.send_keys("cheese!")

		# submit the form (although google automatically searches now without submitting)
		inputElement.submit()

		# the page is ajaxy so the title is originally this:
		print( self.driver.title )

		try:
		    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
		    WebDriverWait(self.driver, 10).until(EC.title_contains("cheese!"))

		    # You should see "cheese! - Google Search"
		    print( self.driver.title )
		    self.assertTrue(  self.driver.title.find(  "cheese!" ) != -1 )

		finally:
		    self.driver.quit()


        
class Test_Chrome(Test_FireFox):

	driver = webdriver.Chrome()





if __name__ == '__main__':
	unittest.main()