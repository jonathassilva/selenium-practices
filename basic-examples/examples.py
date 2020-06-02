import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Exemplo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    
    def test_abrir_pagina(self):
        self.driver.get("http://www.google.com")
        assert "Google" in self.driver.title, "Teste falhou"


    def test_buscar_enter(self):
        self.driver.get("http://www.google.com")
        element = self.driver.find_element_by_name('q')
        element.send_keys("selenium")
        element.send_keys(Keys.RETURN)
        assert "selenium" in self.driver.page_source, "Teste falhou"
   
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
