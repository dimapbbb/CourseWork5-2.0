from abc import ABC, abstractmethod
from src.config import config
from src.employer import Employer
from src.parser import HH
from src.vacancy import Vacancy

import psycopg2


class FileWork(ABC):
    @abstractmethod
    def save_vacancy(self, vacancy):
        pass

    @abstractmethod
    def save_employer(self, employer):
        pass


class FileWorkSQL(FileWork, HH):
    """
    Класс для работы с базой данных
    """
    def __init__(self):
        self.conn_params = config()
        super().__init__()

    def create_table_employers(self):
        """Create table_employers"""
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                query = (f"drop table employers cascade;"
                         f"create table employers "
                         f"("
                         f"employer_id varchar(10) PRIMARY KEY,"
                         f"employer_name text,"
                         f"open_vacancies smallint,"
                         f"vacancies_url varchar(100)"
                         f")")
                cur.execute(query)
                conn.commit()

    def create_table_vacancies(self):
        """Create table_vacancies"""
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                query = (f"drop table vacancies;"
                         f"create table vacancies "
                         f"("
                         f"vacancy_name text,"
                         f"area text,"
                         f"salary int,"
                         f"vacancy_url varchar(100),"
                         f"employer_id varchar(10) references employers(employer_id) not null"
                         f")")
                cur.execute(query)
                conn.commit()

    def save_employer(self, employer: Employer):
        """save employer to database"""
        query = (f"INSERT INTO employers VALUES ("
                 f"'{employer.employer_id}', "
                 f"'{employer.name}', "
                 f"'{employer.open_vacancies}', "
                 f"'{employer.vacancies_url}')")

        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                conn.commit()

    def save_vacancy(self, vacancy: Vacancy):
        """save vacancy ti database"""
        query = (f"INSERT INTO vacancies VALUES ("
                 f"'{vacancy.name}', "
                 f"'{vacancy.area}', "
                 f"'{vacancy.salary}', "
                 f"'{vacancy.url}', "
                 f"'{vacancy.employer_id}')")

        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                conn.commit()
