from selenium.webdriver.common.by import By

class LocatorsBurgers:

    STELLAR_BURGERS_LOGIN = (By.NAME, "name")    #поле логина
    STELLAE_BURGERS_PASSWORD = (By.NAME, "Пароль")    #поле пароля
    STELLAR_BURGERS_BUTTON_ENTER_ENTER = (By.XPATH, ".//button[text() = 'Войти']")  # кнопка "Войти"
                                                                                                    # на странице "Вход"
    STELLAR_BURGERS_BUTTON_START_WINDOW_ENTER = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  #кнопка "Войти в
                                                                                        # аккаунт" на стартовой странице
    STELLAR_BURGERS_BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # кнопка "Личный кабинет"
    STELLAR_BURGERS_BUTTON_REGISTER = (By.XPATH, ".//a[text()='Зарегистрироваться']")   #  кнопка "Зарегистрироваться"
    STELLAR_BURGERS_BUTTON_ENTER = (By.XPATH, ".//a[text()='Войти']")   #  кнопка "Войти" в форме регистрации
    STELLAR_BURGERS_BUTTON_PASSWORD_RECOVERY = (By.XPATH, ".//a[text()='Восстановить пароль']")  # Кнопка
                                                                                             # "Восстановления пароля"
    STELLAR_BURGERS_BUTTON_ENTER_RECOVERY_FORM = (By.XPATH, ".//a[text()='Войти']") # Кнопка "Войти" в форме
                                                                                                # восстановления пароля
    STELLAR_BURGERS_BUTTON_DESIGNER = (By.XPATH, ".//p[text()= 'Конструктор']") # Кнопка "Конструктор"
    STELLAR_BURGERS_TITLE_ASSEMBLE_THE_BURGER = (By.XPATH, ".//h1")  # Надпись, "Соберите бургер"
    STELLAR_BURGERS_LOGO = (By.XPATH, ".//div[contains(@class,'logo')]")  # Логотип "Stellar Burgers"
    STELLAR_BURGERS_BUTTON_EXIT = (By.XPATH, ".//button[text()='Выход']")  #  Кнопка "Выход"
    STELLAR_BURGERS_BUTTON_SAUCES = (By.XPATH, ".//span[text()='Соусы']") # Кнопка раздела "Соусы"
    STELLAR_BURGERS_BUTTON_FILLINGS = (By.XPATH, ".//span[text()='Начинки']")  # Кнопка раздела "Начинки"
    STELLAR_BURGERS_BUTTON_ROLLS = (By.XPATH, ".//span[text()='Булки']") # Кнопка раздела "Булки"
    STELLAR_BURGERS_ACTIVE_BUTTON_ROLLS = (By.XPATH, ".//main//div[1][contains(@class, 'current')]") # Активная кнопка
                                                                                                    # раздела "Булки"
    STELLAR_BURGERS_ACTIVE_BUTTON_SAUCES = (By.XPATH, ".//main//div[2][contains(@class, 'current')]") # Активная кнопка
                                                                                                    # раздела "Соусы"
    STELLAR_BURGERS_ACTIVE_BUTTON_FILLINGS = (By.XPATH, ".//main//div[3][contains(@class, 'current')]") # Активная
                                                                                            # кнопка раздела "Начинки"
    STELLAR_BURGERS_TITLE_ENTER = (By.XPATH, ".//h2[text()='Вход']") # Надпись "Вход"
    STELLAR_BURGERS_TITLE_PROFILE = (By.XPATH, ".//a[contains(@href, 'profile')]") # Надпись профиль
    STELLAR_BURGERS_TITLE_RECOVERY_PASSWORD = (By.XPATH, ".//h2[text()='Восстановление пароля']") # Надпись
                                                                                            # "Восстановление пароля"
    STELLAR_BURGERS_TITLE_REGISTER = (By.XPATH, ".//h2[text()='Регистрация']") # Надпись "Регистрация"
    STELLAR_BURGERS_HOLDER_REGISTER_NAME = (By.XPATH, ".//fieldset[1]//input") # Холдер "Name" в форме регистрации
    STELLAR_BURGERS_HOLDER_REGISTER_MAIL = (By.XPATH, ".//fieldset[2]//input") # Холдер "mail" в форме регистрации
    STELLAR_BURGERS_HOLDER_REGISTER_PASSWORD = (By.XPATH, ".//fieldset[3]//input") # Холдер "password" в форме регистрации
    STELLAR_BURGERS_BUTTON_REGISTER_FORM_REGISTER = (By.XPATH, ".//button[text()= 'Зарегистрироваться']") # Кнопка
                                                                            # "Зарегистрироваться" в форме регистрации
    STELLAR_BURGERS_FORM_REGISTER_WRONG_PASSWORD = (By.XPATH, ".//p[text() = 'Некорректный пароль']") # Надпись
                                                                                                # "Некорректный пароль"