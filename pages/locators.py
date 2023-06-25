from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    FILTER_BY_TYPE = (By.CSS_SELECTOR, 'div#pv_id_2 > div > span')
    HAMSTER_TYPE = (By.XPATH, '//*[@id="pv_id_2_3"]')
    FILTER_BY_NAME = (By.XPATH, '//*[@id="petName"]')
    DETAILS = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/button')
    PICTURE = (By.CSS_SELECTOR, 'div#app > main > div > div > div > div > div:nth-of-type(2) > span > div')
    PET_NAME = (By.XPATH, '//*[@id="app"]/main/div[1]/div[2]/div/div/div[2]/ul/li[1]/a/span/span[2]')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'login')
    LOGIN_PASS = (By.XPATH, '//*[@id="password"]/input')
    LOGIN_BUTTON = (By.CLASS_NAME, 'p-button-label')


class ProfilePageLocators:
    PROFILE_QUIT = (By.XPATH, '//*[@id="app"]/header/div/ul/li[2]/a')
    EDIT_PET = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-content > div > div:nth-child(1) > div > div.product-list-action > button:nth-child(1)')
    INPUT_NAME = (By.ID, 'name')
    SAVE_BUTTON = (By.XPATH, '// *[ @ id = "app"] / main[1] / div[1] / form[1] / div[1] / div[2] / div[3] / button[1] / span[2]')
    DELETE_PET = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[1]/div/div[2]/button[2]')
    ADD_PET = (By.XPATH, '//*[@id="app"]/main/div/div/div[1]/div/div[1]/button')
    CANCEL_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[2]')