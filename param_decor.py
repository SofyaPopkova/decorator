import datetime
import requests

FINAL_FILE = 'final.txt'


def path_log(path):
    def logger(function):
        cache = None
        counter = 0
        cache_time = datetime.datetime.now()

        def new_function(*args, **kwargs):
            nonlocal cache
            nonlocal counter
            if cache is None:
                cache = function(*args, **kwargs)
            counter += 1
            result = function(*args, **kwargs)
            with open(FINAL_FILE, 'a', encoding='utf-8') as f:
                f.write(f'Вызов № {counter}, Дата: {cache_time.date()}, '
                        f'Время: {cache_time.time()}, Название: {function.__name__}, Аргументы: {args}, '
                        f'Возвращаемое значение: {result}\n')
            return result
        return new_function
    return logger


@path_log(r'C:\Project\decorate\final.txt')
def get_status(*args):
    print('Вызвана тестовая функция')
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code


if __name__ == '__main__':
    get_status('https://yandex.ru/')
    get_status('https://netology.ru/')
    get_status('https://dogstudio.co/404/')
