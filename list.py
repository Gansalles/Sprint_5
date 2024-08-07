import random
import string


class List:
    @staticmethod
    def name():
        names = ['Bob', 'Ilan', 'Alex', 'Vlad', 'Maks']
        random_name = random.choice(names)
        return f'{random_name}'


    @staticmethod
    def mail():
        names = ['Bob', 'Ilan', 'Alex', 'Vlad', 'Maks']
        random_name = random.choice(names)
        data = random.randint(1900, 2024)
        domains = ['yandex.ru', 'mail.ru', 'gmail.com', 'yahoo.ru']
        random_domain = random.choice(domains)
        return f'{random_name}-{data}@{random_domain}'


    @staticmethod
    def correct_password():
        correct_password = random.randint(000000, 999999)
        return f'{correct_password}'

    @staticmethod
    def wrong_password():
        wrong_password = random.randint(0000, 9999)
        return f'{wrong_password}'