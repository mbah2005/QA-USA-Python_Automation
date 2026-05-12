import data
import helpers
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

        # Check if the application server is reachable before starting tests
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print('Connected to Urban Routes Server')
        else:
            print('Cannot connect to Urban Routes. Check the server is on and still running')

    def test_set_route(self):
        # Tests that the 'From' and 'To' addresses are correctly entered and displayed
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        main_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert main_page.get_from_address_text() == data.ADDRESS_FROM
        assert main_page.get_to_address_text() == data.ADDRESS_TO


    def test_select_plan(self):
        # Verifies that the 'Supportive' tariff plan can be selected
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        main_page.select_supportive_plan(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert 'Supportive' in main_page.get_supportive_text()


    def test_fill_phone_number(self):
        # Confirms that the user's phone number is correctly populated in the profile
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        main_page.input_phone_number(data.ADDRESS_FROM, data.ADDRESS_TO, data.PHONE_NUMBER)
        assert main_page.get_phone_number() == data.PHONE_NUMBER


    def test_fill_card(self):
        # Validates the process of adding a credit card as a payment method
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        main_page.add_credit_card(data.ADDRESS_FROM, data.ADDRESS_TO, data.CARD_NUMBER, data.CARD_CODE)
        assert 'Card' in main_page.get_payment_method()


    def test_comment_for_driver(self):
        # Tests the ability to leave a text comment/message for the taxi driver
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        main_page.add_comment_for_driver(data.ADDRESS_FROM, data.ADDRESS_TO, data.MESSAGE_FOR_DRIVER)
        assert main_page.get_comment() == data.MESSAGE_FOR_DRIVER


    def test_order_blanket_and_handkerchiefs(self):
        # Verifies that the optional 'blanket and handkerchiefs' item can be toggled
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        main_page.add_blanket_and_handkerchief(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert main_page.verify_checkbox()


    def test_order_2_ice_creams(self):
        # Tests the counter functionality by ordering exactly 2 ice creams
        number_of_ice_creams = 2
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        main_page.add_ice_cream(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Loop to click the increment button based on the required quantity
        for i in range(number_of_ice_creams):
            main_page.click_counter_button()
            time.sleep(1)
        assert '2' in main_page.get_icecream_value()


    def test_car_search_model_appears(self):
        # Final flow test: triggers the order and checks if the car search modal/overlay appears
        main_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        main_page.order_taxi(data.ADDRESS_FROM, data.ADDRESS_TO, data.PHONE_NUMBER, data.MESSAGE_FOR_DRIVER)
        assert main_page.get_car_search()



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()