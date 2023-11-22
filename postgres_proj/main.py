from hh_agent import HH_Api
from dbmanager import DB_MANAGER

"""
Демонстрация всего функционала
"""
db_manager = DB_MANAGER()
count = int(input())
kwords = input()
db_manager.load_vacancies(count, kwords)
print(db_manager.get_avg_salary())
print(db_manager.get_all_vacancies())
print(db_manager.get_companies_and_vacancies_count())
print(db_manager.get_vacancies_with_higher_salary())
kwords = input().split()
print(db_manager.get_vacancies_with_keyword(kwords))
