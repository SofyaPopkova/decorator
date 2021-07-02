import datetime
from pip._vendor import requests

FINAL_FILE = r'C:\Project\decorate\final.txt'


def path_log(path):
    def logger(function):
        counter = 0

        def new_function(*args, **kwargs):
            nonlocal counter
            counter += 1
            cache_time = datetime.datetime.now()
            result = function(*args, **kwargs)
            with open(FINAL_FILE, 'a', encoding='utf-8') as f:
                f.write(f'Вызов № {counter}, Дата: {cache_time.date()}, '
                        f'Время: {cache_time.time()}, Название: {function.__name__}, Аргументы: {args}, '
                        f'Возвращаемое значение: {result}, Путь к файлу: {path}\n')
            return result
        return new_function
    return logger


@path_log(path=FINAL_FILE)
def get_status(*args):
    print('Вызвана тестовая функция')
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code


if __name__ == '__main__':
    get_status('https://yandex.ru/')
    get_status('https://netology.ru/')
    get_status('https://dogstudio.co/404/')
