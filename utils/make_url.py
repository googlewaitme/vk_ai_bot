class Utils:
    def __init__(self):
        self.key = "url_to_cite"
        self.url_base = "https://my.incognitocr.ru/#/loan-vk?"

        "phone=9991231212&birth_date=2000-01-01&sum=1&days=50"

    def make(self, data):
        # TODO Расчёт периода
        # обработка номера телефона 
        # получение конктреного числа для количества
        # Дату рождения тоже обработчик нужно добавить
        phone = data['phone']
        period = data['period']  # TODO me
        amount = data['amount']
        birthday = data['birthday']
        days = 1
        url = self.url_base[:]
        url += f'phone={phone}'
        url += f"&birth_date={birthday}"
        url += f"&sum={amount}"
        url += f"&days={days}"
        return url
