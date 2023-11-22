from hh_agent import HH_Api
from dbmanager import DB_MANAGER


db_manager = DB_MANAGER()
print(db_manager.get_vacancies_with_keyword(['python']))
