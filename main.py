from data import URBAN_ROUTES_URL, ADDRESS_FROM, ADDRESS_TO, PHONE_NUMBER, CARD_NUMBER, CARD_CODE, MESSAGE_FOR_DRIVER
from helpers import is_url_reachable, retrieve_phone_code
from selenium.webdriver.common.by import By

from selenium import webdriver

import time
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        if is_url_reachable(URBAN_ROUTES_URL):
            print('Connected to Urban Routes Server')
        else:
            print('Cannot connect to Urban Routes. Check the server is on and still running')

    def test_set_route(self):
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        main_page.enter_locations(ADDRESS_FROM, ADDRESS_TO)
        assert self.driver.find_element(By.ID, "from").get_attribute("value") == ADDRESS_FROM
        assert self.driver.find_element(By.ID, "to").get_attribute("value") == ADDRESS_TO


    def test_select_plan(self):
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        main_page.select_supportive_plan(ADDRESS_FROM, ADDRESS_TO)
        actual_value = main_page.get_supportive_text()
        expected_value = 'Supportive'
        assert expected_value in actual_value, f"Expected {expected_value} but got {actual_value}"

    def test_fill_phone_number(self):
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        main_page.select_supportive_plan(ADDRESS_FROM, ADDRESS_TO)
        main_page.input_phone_number(PHONE_NUMBER)
        assert self.driver.find_element(By.CLASS_NAME, 'np-text').text == PHONE_NUMBER



    def test_fill_card(self):
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        main_page.select_supportive_plan(ADDRESS_FROM, ADDRESS_TO)
        main_page.add_credit_card(CARD_NUMBER, CARD_CODE)
        actual_value = main_page.get_payment_method()
        expected_value = 'Card'
        assert expected_value in actual_value, f"Expected {expected_value} but got {actual_value}"


    def test_comment_for_driver(self):
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        main_page.add_comment_for_driver(ADDRESS_FROM, ADDRESS_TO, MESSAGE_FOR_DRIVER)
        assert main_page.get_comment() == MESSAGE_FOR_DRIVER


    def test_order_blanket_and_handkerchiefs(self):
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        main_page.add_blanket_and_handkerchief(ADDRESS_FROM, ADDRESS_TO)
        assert main_page.verify_checkbox()


    def test_order_2_ice_creams(self):
        number_of_ice_creams = 2
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        main_page.add_ice_cream(ADDRESS_FROM, ADDRESS_TO)
        for i in range(number_of_ice_creams):
            main_page.click_counter_button()
        actual_value = main_page.get_icecream_value()
        expected_value = '2'
        assert expected_value in actual_value, f"Expected {expected_value} but got {actual_value}"

    def test_car_search_model_appears(self):
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        main_page.order_taxi(ADDRESS_FROM, ADDRESS_TO, PHONE_NUMBER, MESSAGE_FOR_DRIVER)
        assert main_page.get_car_search() == True



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()