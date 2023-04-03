from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    BUTTON_PEOPLE = (By.XPATH, '//*[@id="root"]/div/div/header/div/div[1]/div[4]/div/button/svg')
    BUTTON_REGIST = (By.XPATH, '//*[@id="root"]/div/div/header/div/div[1]/div[4]/div/ul/li[2]/a')
    BUTTON_SIGN = (By.XPATH, '//*[@id="root"]/div/div/main/div[2]/button[2]')
    BUTTON_IAMHERE = (By.XPATH, '//*[@id="root"]/div/div/main/div[3]/button[1]')
    INPUT_VALID_EMAIL = (By.XPATH, '//*[@id="root"]/div/div/main/form/div[1]/input')
    INPUT_PASS = (By.XPATH, '//*[@id="root"]/div/div/main/form/div[2]/div[1]/input')
    BUTTON_CONTINUE = (By.XPATH, '//*[@id="root"]/div/div/main/form/button')
    BUTTON_IAMTOSELL = (By.XPATH, '//*[@id="root"]/div/div/main/div[3]/button[2]')
    BUTTON_LOGIN = (By.XPATH, '//*[@id="root"]/div/div/main/div[2]/button[1]')
    BUT_FORGOT_PASS = (By.XPATH, '//*[@id="root"]/div/div/main/div[3]/a')
    INPUT_FORGOT_EMAIL = (By.XPATH, '//*[@id="root"]/div/div/div[3]/form/div/input')
    BUTTON_RESETPASS = (By.XPATH, '//*[@id="root"]/div/div/div[3]/form/button')
    BUTTON_REGSTRATION = (By.XPATH, '//*[@id="root"]/div/div/header/div/div[1]/div[4]/div/ul/li[2]/a')
