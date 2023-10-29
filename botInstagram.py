from selenium import webdriver
import time
import random


class OnetRegister():

    def __init__(self):
        self.windows = webdriver.Chrome()

    def login(self):
        self.login = "your_login"
        self.password = "your_password"


        self.windows.get("https://www.instagram.com/")
        self.changeTime = random.randint(4,7)
        time.sleep(self.changeTime)
        try:
            self.cookie = self.windows.find_element("xpath",'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
            self.cookie.click()
            time.sleep(self.changeTime)
        except:
            self.cookie = self.windows.find_element("xpath", '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
            self.cookie.click()
            time.sleep(self.changeTime)
        finally:
            time.sleep(self.changeTime)

        try:
            self.emailForm = self.windows.find_element("xpath",'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
            self.emailForm.click()
            time.sleep(self.changeTime)
            self.emailForm.send_keys(self.login)
        except:
            self.emailForm = self.windows.find_element("xpath",'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
            self.emailForm.click()
            time.sleep(self.changeTime)
            self.emailForm.send_keys(self.login)

        finally:
            time.sleep(self.changeTime)


        try:
            self.passwordForm = self.windows.find_element("xpath",'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
            self.passwordForm.click()
            time.sleep(self.changeTime)
            self.passwordForm.send_keys(self.password)
        except:
            self.passwordForm = self.windows.find_element("xpath",'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
            self.passwordForm.click()
            time.sleep(self.changeTime)
            self.passwordForm.send_keys(self.password)
        finally:
            time.sleep(self.changeTime)
        try:
            self.buttonLogin = self.windows.find_element("xpath",'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]')
            time.sleep(self.changeTime)
            self.buttonLogin.click()
        except:
            self.buttonLogin = self.windows.find_element("xpath",'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]')
            time.sleep(self.changeTime)
            self.buttonLogin.click()
        finally:
            time.sleep(10)

        try:
            self.buttonNotNow = self.windows.find_element("xpath",'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
            time.sleep(self.changeTime)
            self.buttonNotNow.click()
        except:
            self.buttonNotNow = self.windows.find_element("xpath",'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
            time.sleep(self.changeTime)
            self.buttonNotNow.click()
        finally:
            time.sleep(13)

        try:
            self.turnOn = self.windows.find_element("xpath",
                                                          '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]')
            time.sleep(self.changeTime)
            self.turnOn.click()
        except:
            self.turnOn = self.windows.find_element("xpath",
                                                          '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]')
            time.sleep(self.changeTime)
            self.turnOn.click()
        finally:
            time.sleep(11)




        time.sleep(11000)
botOn = OnetRegister()
botOn.login()