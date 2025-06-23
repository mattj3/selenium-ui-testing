def test_successful_login(driver, base_url, username, password):
    driver.get(base_url)
    driver.find_element("id", "user-name").send_keys(username)
    driver.find_element("id", "password").send_keys(password)
    driver.find_element("id", "login-button").click()
    assert "inventory" in driver.current_url
