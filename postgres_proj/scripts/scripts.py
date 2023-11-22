from dbmanager import DB_MANAGER

def get_companies_and_vacancies_count():
    db_manager = DB_MANAGER()
    print(db_manager.get_companies_and_vacancies_count())
