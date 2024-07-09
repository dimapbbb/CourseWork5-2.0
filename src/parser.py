from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    @abstractmethod
    def load_employer(self, employer_id):
        pass

    @abstractmethod
    def load_vacancies(self, employer_id):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """
    def __init__(self):
        self.url = 'https://api.hh.ru/'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}

    def load_employer(self, employer_id):
        """load_employer info from employer_id"""
        url = self.url + "employers/" + employer_id
        response = requests.get(url, headers=self.headers, params=self.params)
        return response.json()

    def load_vacancies(self, employer_id):
        """load vacancies from employer_id"""
        url = self.url + 'vacancies?employer_id=' + employer_id
        vacancies_list = []

        while self.params["page"] != 20:
            response = requests.get(url, headers=self.headers, params=self.params)
            vacancies = response.json()["items"]
            vacancies_list.extend(vacancies)
            self.params['page'] += 1
        return vacancies_list

