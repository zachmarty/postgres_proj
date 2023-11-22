from dbmanager import DB_MANAGER


def get_companies_and_vacancies_count():
    """
    Функция для получения количества работодателей и вакансий
    """
    db_manager = DB_MANAGER()
    print(db_manager.get_companies_and_vacancies_count())

def get_all_vacancies():
    """
    Функция для получения всех вакансий
    """
    db_manager = DB_MANAGER()
    print(db_manager.get_all_vacancies())

def get_avg_salary():
    """
    Функция для получения средней зарплаты
    """
    db_manager = DB_MANAGER()
    print(db_manager.get_avg_salary())

def get_vacancies_with_higher_salary():
    """
    Функция для получения вакансий с зарплатой выше средней
    """
    db_manager = DB_MANAGER()
    print(db_manager.get_vacancies_with_higher_salary())

def get_vacancies_with_keyword():
    """
    Функция для получения вакансий по ключевым словам
    """
    kwords = input().split()
    db_manager = DB_MANAGER()
    print(db_manager.get_vacancies_with_keyword(kwords))

def load_vacancies():
    """
    Функция для загрузки и записи вакансий в базу данных
    """
    count = int(input())
    kwords = input()
    db_manager = DB_MANAGER()
    db_manager.load_vacancies(count, kwords)