import unittest2
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleSearchTest(unittest2.TestCase):
 
    def setUp(self):
        # Create a new Firefox driver instance
        self.driver = webdriver.Firefox(executable_path=r'/home/testanimesh26/geckodriver')

    def tearDown(self):
        # Close the browser after running the tests
        self.driver.quit()

    def testSearch(self):
        # Trigger a Google Search
        self.driver.get('http://www.google.com')
        self.assertEqual(self.driver.title, 'Google')
        searchElement = self.driver.find_element_by_name('q')
        searchElement.send_keys('Animesh Kumar Sahu')
        searchElement.submit()
        WebDriverWait(self.driver, 30).until(EC.title_contains('Animesh Kumar Sahu'))
        self.assertTrue(self.driver.title.startswith('Animesh Kumar Sahu'))
