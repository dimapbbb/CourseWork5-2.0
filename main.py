from src.DBManager import DBManager
from src.employer import Employer
from src.vacancy import Vacancy


def main():
    employer_ids = ["9764865", "1490605", "1373", "5124731", "9202128", "112324", "17831", "193400", "869045", "1923"]
    user = DBManager()

    user.create_table_employers()
    user.create_table_vacancies()

    for employer_id in employer_ids:
        employer_info = user.load_employer(employer_id)
        employer = Employer.new_employer(employer_info)
        user.save_employer(employer)

        vacancies = user.load_vacancies(employer_id)
        for vacancy in vacancies:
            vac = Vacancy.new_vacancy(vacancy)
            user.save_vacancy(vac)

    # test = user.get_companies_and_vacancies_count()
    # for row in test:
    #     print(row)


if __name__ == "__main__":
    main()
