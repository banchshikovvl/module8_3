class Car:
    def __init__(self, model: str, __vin: int, __numbers: str):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(__numbers)

    def __is_valid_vin(self, __vin):
        if isinstance(__vin, int):
            if 1000000 <= __vin <= 9999999:
                return True
            else:
                raise IncorrectVinNumber(f'{self.model}, Неверный диапазон для vin номера: "{self.__vin}"')
        else:
            raise IncorrectVinNumber(f'{self.model}, Некорректный тип vin номер: "{self.__vin}"')

    def __is_valid_numbers(self, __numbers):
        if isinstance(__numbers, str):
            if len(__numbers) == 6:
                return True
            else:
                raise IncorrectCarNumbers(f'{self.model}, Неверная длина номера: "{self.__numbers}"')
        else:
            raise IncorrectCarNumbers(f'{self.model}, Некорректный тип данных для номеров: {self.__numbers}')

    def getter(self):
        return f'Vin: {self.__vin}, Гос.номер: {self.__numbers}'


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model}, {first.getter()}, успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model}, {second.getter()}, успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model}, {third.getter()}, успешно создан')
