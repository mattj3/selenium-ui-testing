class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com"
        self.username_input_id = "user-name"
        self.password_input_id = "password"
        self.login_button_id = "login-button"

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element("id", self.username_input_id).send_keys(username)
        self.driver.find_element("id", self.password_input_id).send_keys(password)
        self.driver.find_element("id", self.login_button_id).click()
