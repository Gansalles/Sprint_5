from selenium.webdriver.common.by import By

class LocatorsBurgers:

    stellar_burgers_login = (By.NAME, "name")    #поле логина
    stellar_burgers_password = (By.NAME, "Пароль")    #поле пароля
    stellar_burgers_button_enter_enter = (By.XPATH, ".//button[text() = 'Войти']")  # кнопка "Войти"
                                                                                                    # на странице "Вход"
    stellar_burgers_button_start_window_enter = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  #кнопка "Войти в
                                                                                        # аккаунт" на стартовой странице
    stellar_bugrers_button_personal_account = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # кнопка "Личный кабинет"
    stellar_bugrers_button_register = (By.XPATH, ".//a[text()='Зарегистрироваться']")   #  кнопка "Зарегистрироваться"
    stellar_bugrers_button_enter = (By.XPATH, ".//a[text()='Войти']")   #  кнопка "Войти" в форме регистрации
    stellar_bugrers_button_password_recovery = (By.XPATH, ".//a[text()='Восстановить пароль']")  # Кнопка
                                                                                             # "Восстановления пароля"
    stellar_bugrers_button_enter_recovery_form = (By.XPATH, ".//a[text()='Войти']") # Кнопка "Войти" в форме
                                                                                                # восстановления пароля
    stellar_bugrers_button_designer = (By.XPATH, ".//p[text()= 'Конструктор']") # Кнопка "Конструктор"
    stellar_bugrers_title_assemble_the_burger = (By.XPATH, ".//h1")  # Надпись, "Соберите бургер"
    stellar_bugrers_logo = (By.XPATH, ".//div[contains(@class,'logo')]")  # Логотип "Stellar Burgers"
    stellar_bugrers_button_exit = (By.XPATH, ".//button[text()='Выход']")  #  Кнопка "Выход"
    stellar_bugrers_botton_sauces = (By.XPATH, ".//span[text()='Соусы']") # Кнопка раздела "Соусы"
    stellar_bugrers_button_fillings = (By.XPATH, ".//span[text()='Начинки']")  # Кнопка раздела "Начинки"
    stellar_bugrers_button_rolls = (By.XPATH, ".//span[text()='Булки']") # Кнопка раздела "Булки"