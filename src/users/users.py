from random import randint


class User:
    '''Создание пользователя для сохранения в системе.'''

    def __init__(self, key):
        self.key = key
        self.pin = self._generate_pin()

    def _generate_pin(self):
        '''Генерация pin.'''
        return ''.join([str(randint(0, 9)) for _ in range(4)])
