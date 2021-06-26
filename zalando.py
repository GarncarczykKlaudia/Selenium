import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


#DANE TESTOWE
client_name_valid = "Klaudia"
#client_surname_valid = "Test"
client_email_valid = "klaudia.test@op.pl"
client_pwd_valid = "test1234"

#PRZYPADEK TESTOWY 002
#Rejestracja bez podania nazwiska
#Oczekiwany rezultat
#Komunikat "pole obowiazkowe" oraz komunikat "Naziwsko lub firma cd*"

#WARUNKI WSTĘPNE:
#Przeglądarka jest uruchomiona
#Strona https://www.zalando.pl jest otworzona
#Użytkownik jest niezalogowany

#KROKI

#1. Otworzenie przeglądarki na stronie https://www.zalando.pl
class ZalandoRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.zalando.pl")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.actions = ActionChains(self.driver)

    def testNoEmail(self):
        driver = self.driver
        actions = self.actions


        person_icon = driver.find_element_by_xpath('//div[contains(@class,"z-navicat-header_navToolItem-profile")]')
        actions.move_to_element(person_icon).perform()
        sleep(3)
        new_client_btn = driver.find_element_by_xpath('//a[contains(@class,"z-navicat-header_userAccountRegister")]')
        new_client_btn.click()
        sleep(6)

        personalisation_approval_btn = driver.find_element_by_id('uc-btn-accept-banner')
        personalisation_approval_btn.click()

        imie_field = driver.find_element_by_name('register.firstname')
        imie_field.send_keys(client_name_valid)

        email_field = driver.find_element_by_name('register.email')
        email_field.send_keys(client_email_valid)

        pwd_field = driver.find_element_by_name('register.password')
        pwd_field.location_once_scrolled_into_view
        pwd_field.send_keys(client_pwd_valid)
        sleep(3)

        imie_field.location_once_scrolled_into_view

        register_btn = driver.find_element_by_xpath('//button[contains(@data-testid,"register_button")]')
        register_btn.click()

        sleep(3)

        #TESTY

        red_alert_field_desc = driver.find_element_by_xpath('//label[contains(@class,"AQOYO6")]')
        print(red_alert_field_desc.get_attribute("innerText"))
        #czy to element z wskazanym tekstem
        self.assertEqual(red_alert_field_desc.get_attribute("innerText"),"Nazwisko lub firma cd.*",msg='Błędny komunikat')
        #czy element jest widoczny
        self.assertEqual(red_alert_field_desc.is_displayed(),True)


        red_alert_field_obligatory = driver.find_element_by_xpath('//span[contains(@class,"IwlAj4")]')

        print(red_alert_field_obligatory.get_attribute("innerText"))
        self.assertEqual(red_alert_field_obligatory.get_attribute("innerText"),"Pole obowiązkowe")
        #czy element jest widoczny
        self.assertEqual(red_alert_field_obligatory.is_displayed(),True)


        red_alert_icon = driver.find_element_by_xpath('//*[contains(@class,"emnkVg")]')
        #czy element jest widoczny
        self.assertEqual(red_alert_icon.is_displayed(),True)

        #kontrola ilosci

        fields_desc = driver.find_elements_by_xpath('//label[contains(@class,"AQOYO6")]')
        fields_obligatory = driver.find_elements_by_xpath('//span[contains(@class,"IwlAj4")]')
        alert_icons = driver.find_elements_by_xpath('//*[contains(@class,"emnkVg")]')

        visible_fields_desc = list()
        visible_fields_obligatory = list()
        visible_alert_icons = list()

        for fielda in fields_desc:
            if fielda.is_displayed():
                visible_fields_desc.append(fielda)

        for fieldb in fields_obligatory:
            if fieldb.is_displayed():
                visible_fields_obligatory.append(fieldb)

        for fieldc in alert_icons:
            if fieldc.is_displayed():
                visible_alert_icons.append(fieldc)


        assert len(visible_fields_desc) == 1, "liczba widocznych komunikatow  opis pola nie zgadza sie"
        assert len(visible_fields_obligatory) == 1, "liczba widocznych komunikatow  pole wymagane nie zgadza sie"
        assert len(visible_alert_icons) == 1, "liczba widocznych ikon nie zgadza sie"


    def tearDown(self):
        #zakonczenie testu
        self.driver.quit()

#jesli uruchamiany z tego pliku
if __name__ == "__main__":
    #uzyjmy metody main(), ktora zajmie sie reszta
    unittest.main(verbosity=2)
