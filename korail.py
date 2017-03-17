from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class Korail:
    DOMAIN = 'http://www.letskorail.com'
    LOGIN_URI = '/korail/com/login.do'

    def __init__(self, driver):
        self.driver = driver
        pass

    def login(self, userid, password):
        self.driver.get(self.DOMAIN+self.LOGIN_URI)
        input_id = self.driver.find_element_by_id('txtMember')
        input_pw = self.driver.find_element_by_id('txtPwd')
        input_id.send_keys(userid)
        input_pw.send_keys(password)
        self.driver.execute_script('Login(1)')

        wait = WebDriverWait(self.driver, 2)
        try:
            alert = wait.until(EC.alert_is_present())
            alert.accept()
        except TimeoutException:
            pass

        login_result = self.driver.find_elements_by_xpath("//ul[@class='gnb_list']/li[@class='log_nm']")

        return len(login_result) > 0


if __name__ == "__main__":
    id = '0661086375'
    pw = 'dueksvhT9'
    driver = webdriver.Chrome("D:\\WebDrivers\\chromedriver.exe")
    #driver = webdriver.PhantomJS("D:\\WebDrivers\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")

    korail = Korail(driver)
    print(korail.login(id, 1234))

