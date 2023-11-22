from dbmanager import DB_MANAGER

def get_companies_and_vacancies_count():
    db_manager = DB_MANAGER()
    print(db_manager.get_companies_and_vacancies_count())

def get_all_vacancies():
    db_manager = DB_MANAGER()
    print(db_manager.get_all_vacancies())

def get_avg_salary():
    db_manager = DB_MANAGER()
    print(db_manager.get_avg_salary())

def get_vacancies_with_higher_salary():
    db_manager = DB_MANAGER()
    print(db_manager.get_vacancies_with_higher_salary())

def get_vacancies_with_keyword():
    kwords = input().split()
    db_manager = DB_MANAGER()
    print(db_manager.get_vacancies_with_keyword(kwords))

def load_vacancies():
    count = int(input())
    kwords = input()
    db_manager = DB_MANAGER()
    db_manager.load_vacancies(count, kwords)