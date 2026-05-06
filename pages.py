from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_LOCATOR = (By.XPATH, '//button[@class = "button round"]')
    SUPPORTIVE_LOCATOR = (By.XPATH, '//div[contains(text(),"Supportive")]')
    PHONE_NUMBER_LOCATOR = (By.XPATH, '//div[@class = "np-button"]')
    ENTER_PHONE_NUMBER_LOCATOR = (By.XPATH, '//div[@class = "input-container"]')
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[@class = "button full"]')
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//div[contains(text(),"Confirm")]')
    PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[contains(text(),"Payment method")]')
    ADD_CARD_LOCATOR = (By.XPATH, '//img[@src = "/static/media/plus.d25b8941.svg"]')
    ENTER_CARD_LOCATOR = (By.ID, 'number')
    ENTER_CODE_LOCATOR = (By.ID, 'code')
    LINK_BUTTON_LOCATOR = (By.XPATH, '//div[contains(text(),"Link")]')
    CLOSE_BUTTON_LOCATOR = (By.XPATH, '//button[@class = "close-button section-close"]')
    COMMENT_LOCATOR = (By.ID, 'comment')
    CHECK_BOX_LOCATOR = (By.CLASS_NAME, 'slider round')
    COUNTER_LOCATOR = (By.CLASS_NAME, 'counter-plus')
    CONFIRM_ORDER_LOCATOR = (By.XPATH, '//button[@class = "smart-button"]')

    def __init__(self, driver):
        self.driver = driver  # Initialize the driver


    def enter_from_location(self, from_text):
        # Enter From
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)


    def enter_to_location(self, to_text):
        # Enter To
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)


    def click_call_taxi(self):
        # Click Custom
        self.driver.find_element(*self.CALL_TAXI_LOCATOR).click()


    def click_supportive_icon(self):
        # Click Drive Icon
        self.driver.find_element(*self.SUPPORTIVE_LOCATOR).click()


    def click_phone_number(self):
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).click()


    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.ENTER_PHONE_NUMBER_LOCATOR).send_keys(phone_number)


    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()


    def enter_code(self, code):
        self.driver.find_element(*self.ENTER_CODE_LOCATOR).send_keys(code)


    def click_confirm_button(self):
        # Enter First Name
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()


    def click_payment_method(self, last_name):
        # Enter Last Name
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()


    def add_card(self):
        # Enter Date of Birth
        self.driver.find_element(*self.ADD_CARD_LOCATOR).click()


    def enter_card_number(self, card_number):
        # Enter Number
        self.driver.find_element(*self.ENTER_CARD_LOCATOR).send_keys(card_number)


    def enter_card_code(self, card_code):
        # Click Add a Driver's License Title
        self.driver.find_element(*self.ENTER_CODE_LOCATOR).send_keys(card_code)


    def click_link_button(self):
        # Click Add Button
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

    def click_close_button(self):
        # Click Add Button
        self.driver.find_element(*self.CLOSE_BUTTON_LOCATOR).click()

    def click_comment_button(self):
        # Click Add Button
        self.driver.find_element(*self.COMMENT_LOCATOR).click()

    def enter_comment(self, comment):
        # Click Add Button
        self.driver.find_element(*self.ENTER_CODE_LOCATOR).send_keys(comment)

    def click_checkbox_button(self):
        # Click Add Button
        self.driver.find_element(*self.CHECK_BOX_LOCATOR).click()

    def click_counter_button(self):
        # Click Add Button
        self.driver.find_element(*self.COUNTER_LOCATOR).click()
        
    def get_verification_text(self):
        # Return the verification text
        return self.driver.find_element(*self.VERIFICATION_TEXT_LOCATOR).text
