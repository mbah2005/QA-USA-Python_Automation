from data import URBAN_ROUTES_URL, ADDRESS_FROM, ADDRESS_TO, PHONE_NUMBER, CARD_NUMBER, CARD_CODE, MESSAGE_FOR_DRIVER
from helpers import is_url_reachable
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
        assert self.driver.find_element(By.ID, "from").get_attribute("value") == "East 2nd Street, 601"
        assert self.driver.find_element(By.ID, "to").get_attribute("value") == "1300 1st St"



    def test_select_plan(self):
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        main_page.select_supportive_plan(ADDRESS_FROM, ADDRESS_TO)

    def test_fill_phone_number(self):
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        main_page.input_phone_number(ADDRESS_FROM, ADDRESS_TO, PHONE_NUMBER,)

    def test_fill_card(self):
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        main_page.add_credit_card(ADDRESS_FROM, ADDRESS_TO, CARD_NUMBER, CARD_CODE)

    def test_comment_for_driver(self):
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        main_page.add_comment_for_driver(ADDRESS_FROM, ADDRESS_TO, MESSAGE_FOR_DRIVER)

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print('function created for set route')
        pass

    def test_order_2_ice_creams(self):
        number_of_ice_creams = 2
        for i in range(number_of_ice_creams):
            # Add in S8
            print('function created for set route')
        pass

    def test_car_search_model_appears(self):
        # Add in S8
        print('function created for set route')
        pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()