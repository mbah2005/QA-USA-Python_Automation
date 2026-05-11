from selenium.webdriver.common.by import By
from helpers import retrieve_phone_code
import time

class UrbanRoutesPage:
    # Locators as class attributes for easy maintenance and central management

    #--- Section: Entering Addresses Locators ---
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')

    #--- Section: Selecting Plan & Modes Locators ---
    CALL_TAXI_LOCATOR = (By.XPATH, '//button[@class = "button round"]')
    SUPPORTIVE_LOCATOR = (By.XPATH, '//div[contains(text(),"Supportive")]')

    #--- Section: Entering Phone Number Locators ---
    PHONE_NUMBER_LOCATOR = (By.CLASS_NAME, 'np-text')
    ENTER_PHONE_NUMBER_LOCATOR = (By.ID, 'phone')
    ENTER_PHONE_CODE = (By.ID, 'code')
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[@class = "button full"]')
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(),"Confirm")]')


    #--- Section: Adding Card Info Locators ---
    PAYMENT_METHOD_LOCATOR = (By.XPATH, '//img[@src = "/static/media/chewron.f3fff088.svg"]')
    RETRIEVE_CARD_TEXT =  (By.XPATH, '//div[@class = "pp-value-text"]')
    ADD_CARD_LOCATOR = (By.XPATH, '//img[@src = "/static/media/plus.d25b8941.svg"]')
    ENTER_CARD_LOCATOR = (By.ID, 'number')
    ENTER_CARD_CODE_LOCATOR = (By.XPATH, '//input[@class="card-input" and @id="code"]')
    ADDING_CARD_LOCATOR = (By.XPATH, '//div[contains(text(),"Adding a card")]')
    LINK_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(),"Link")]')

    #--- Section: Adding Comments Locators ---
    COMMENT_LOCATOR = (By.ID, 'comment')
    CHECK_COMMENT_LOCATOR = (By.XPATH, '//input[@class="input" and @id="comment"]')

    #--- Section: Order Requirements Locators (Extras) ---
    CHECK_BOX_LOCATOR = (By.XPATH, '//span[@class = "slider round"]')
    VERIFY_CHECKBOX_LOCATOR = (By.CSS_SELECTOR, ".switch-input")
    COUNTER_LOCATOR = (By.XPATH, '//div[@class = "counter-plus"]')
    ICE_CREAM_AMOUNT = (By.XPATH, '//div[@class = "counter-value"]')

    #--- Section: Placing Order Locators (Final Step) ---
    CONFIRM_ORDER_LOCATOR = (By.XPATH, '//span[@class = "smart-button-secondary"]')
    CAR_SEARCH_LOCATOR = (By.XPATH, '//div[@class = "order-header-title"]')

    def __init__(self, driver):
        # Initializing the driver instance to be used within the class
        self.driver = driver


    def enter_from_location(self, from_text):
        # Enter text into the 'From' address field
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)


    def enter_to_location(self, to_text):
        # Enter text into the 'To' address field
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def get_from_address_text(self):
        # Retrieve the current value of the 'From' address field for validation
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute("value")


    def get_to_address_text(self):
        # Retrieve the current value of the 'To' address field for validation
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute("value")


    def click_call_taxi(self):
        # Click the main button to open the taxi ordering interface
        self.driver.find_element(*self.CALL_TAXI_LOCATOR).click()


    def click_supportive_icon(self):
        # Click the 'Supportive' plan icon among the available options
        self.driver.find_element(*self.SUPPORTIVE_LOCATOR).click()

    def get_supportive_text(self):
        # Retrieve the text from the selected supportive plan element
        return self.driver.find_element(*self.SUPPORTIVE_LOCATOR).text


    def click_phone_number(self):
        # Click the phone number field to trigger the phone input flow
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).click()


    def enter_phone_number(self, phone_number):
        # Type the phone number into the input field
        self.driver.find_element(*self.ENTER_PHONE_NUMBER_LOCATOR).send_keys(phone_number)

    def get_phone_number(self):
        # Get the text currently displayed in the phone number field
        return self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).text


    def click_next_button(self):
        # Click 'Next' to move to the SMS verification step
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()


    def enter_code(self, code):
        # Enter the verification code received via helper utility
        self.driver.find_element(*self.ENTER_PHONE_CODE).send_keys(code)


    def click_confirm_button(self):
        # Confirm the verification code to link the phone number
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()


    def click_payment_method(self):
        # Open the payment method selection menu
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()


    def click_add_card(self):
        # Click the option to add a new bank card
        self.driver.find_element(*self.ADD_CARD_LOCATOR).click()


    def enter_card_number(self, card_number):
        # Type the card number into the bank card input field
        self.driver.find_element(*self.ENTER_CARD_LOCATOR).send_keys(card_number)


    def enter_card_code(self, card_code):
        # Type the CVC code into the card security field
        self.driver.find_element(*self.ENTER_CARD_CODE_LOCATOR).send_keys(card_code)

    def click_add_card_title(self):
        # Click the modal title to shift focus and enable the Link button
        self.driver.find_element(*self.ADDING_CARD_LOCATOR).click()


    def click_link_button(self):
        # Finalize linking the credit card to the account
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

    def get_payment_method(self):
        # Retrieve the label of the current payment method (e.g., 'Card')
        return self.driver.find_element(*self.RETRIEVE_CARD_TEXT).text

    def enter_comment(self, comment):
        # Type a specific message into the driver comment field
        self.driver.find_element(*self.COMMENT_LOCATOR).send_keys(comment)

    def get_comment(self):
        # Verify the content currently typed in the comment field
        return self.driver.find_element(*self.CHECK_COMMENT_LOCATOR).get_attribute("value")

    def click_checkbox_button(self):
        # Toggle the switch for blankets and handkerchiefs
        self.driver.find_element(*self.CHECK_BOX_LOCATOR).click()

    def verify_checkbox(self):
        # Check the internal state of the checkbox to see if it is enabled
        return self.driver.find_element(*self.VERIFY_CHECKBOX_LOCATOR).get_property('checked')

    def click_counter_button(self):
        # Click the '+' button to increase ice cream count
        self.driver.find_element(*self.COUNTER_LOCATOR).click()

    def get_icecream_value(self):
        # Get the current numeric count of ice creams displayed on the counter
        return self.driver.find_element(*self.ICE_CREAM_AMOUNT).text

    def click_order_button(self):
        # Final confirmation to place the taxi order
        self.driver.find_element(*self.CONFIRM_ORDER_LOCATOR).click()

    def get_car_search(self):
        # Check if the 'searching for car' modal is visible on screen
        return self.driver.find_element(*self.CAR_SEARCH_LOCATOR).is_displayed()



    # --- Combined (Methods that group multiple steps) ---

    def enter_locations(self, from_text, to_text):
        # Complete flow for entering 'From' and 'To' Addresses
        self.enter_from_location(from_text)
        time.sleep(2)
        self.enter_to_location(to_text)
        time.sleep(2)

    def select_supportive_plan(self, from_text, to_text):
        # Complete flow for setting the route and picking the 'Supportive' tariff
        self.enter_locations(from_text, to_text)
        self.click_call_taxi()
        time.sleep(1)
        self.click_supportive_icon()
        time.sleep(2)


    def input_phone_number(self, from_text, to_text, phone_number):
        # Full flow for entering route, picking plan, and verifying phone number
        self.select_supportive_plan(from_text, to_text)
        self.click_phone_number()
        time.sleep(2)
        self.enter_phone_number(phone_number)
        time.sleep(1)
        self.click_next_button()
        time.sleep(2)
        # Fetch the code from server logs using the helper function
        phone_code = retrieve_phone_code(self.driver)
        self.enter_code(phone_code)
        time.sleep(2)
        self.click_confirm_button()
        time.sleep(2)

    def add_credit_card(self,from_text, to_text, card_number, card_code):
        # Full flow for setting route/plan and adding a new payment card
        self.select_supportive_plan(from_text, to_text)
        self.click_payment_method()
        time.sleep(2)
        self.click_add_card()
        time.sleep(2)
        self.enter_card_number(card_number)
        time.sleep(2)
        self.enter_card_code(card_code)
        self.click_add_card_title()
        time.sleep(2)
        self.click_link_button()
        time.sleep(2)

    def add_comment_for_driver(self, from_text, to_text, comment):
        # Flow for adding a comment to a taxi order
        self.select_supportive_plan(from_text, to_text)
        self.enter_comment(comment)
        time.sleep(2)

    def add_blanket_and_handkerchief(self, from_text, to_text):
        # Flow for adding extra requirements (blanket/handkerchiefs)
        self.select_supportive_plan(from_text, to_text)
        self.click_checkbox_button()
        time.sleep(2)

    def add_ice_cream(self, from_text, to_text):
        # Pre-requisite step for ice cream tests (selecting the plan)
        self.select_supportive_plan(from_text, to_text)

    def order_taxi(self, from_text, to_text, phone_number, comment):
        # End-to-end flow to trigger the final taxi search
        self.input_phone_number(from_text, to_text, phone_number)
        self.enter_comment(comment)
        time.sleep(2)
        self.click_order_button()
        time.sleep(2)




