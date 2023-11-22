import requests
import json
from abc import ABC, abstractclassmethod

class Api(ABC):
    """
    Абстрактный класс - база
    """
    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def get_vacancies(self, word):
        pass

class HH_Api(Api):
    """
    Класс для работы с апи на hh.ru
    """
    def __init__(self, count = 10) -> None:
        """
        Конструктор с входным параметром количество вакансий, который устанавливает параметры для гет-запросов
        """
        self.params = {
            'per_page': count,
            'area': 1,
            'page': 1           
        }
        self.url = 'https://api.hh.ru/vacancies/'

    def get_vacancies(self, words = 'Python'):
        """
        Метод для получения вакансий
        """
        self.params['text'] = words
        r = requests.get(self.url, params=self.params)
        return json.loads(r.text)['items']