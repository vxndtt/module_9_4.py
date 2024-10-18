from random import choice


'''Lambda-функция:'''

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


'''Замыкание:'''

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "w", encoding = 'utf-8') as file:
            for string in data_set:
                string = str(string)
                if isinstance(string, list):
                    for object_ in string:
                        object_ = str(object_)
                        file.write(object_ + '\n')
                file.write(string + '\n')
        file.close()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], ['For', 'you'])

'''Метод __call__:'''

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())