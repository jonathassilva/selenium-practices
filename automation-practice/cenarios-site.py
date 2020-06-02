import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class CenariosSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com/index.php")
    
    def test_produto_existente(self):
        search_field = self.driver.find_element_by_id('search_query_top')
        search_button = self.driver.find_element_by_name('submit_search')
        search_field.send_keys('Blouse')
        search_button.click()
        item = self.driver.find_element_by_class_name('product_img_link')
        self.assertTrue(item.is_displayed())
    
    def test_produto_nao_existente(self):
        search_field = self.driver.find_element_by_id('search_query_top')
        search_button = self.driver.find_element_by_name('submit_search')
        search_field.send_keys('Blusa')
        search_button.click()
        self.assertTrue('No results were found for your search' in self.driver.page_source)
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
