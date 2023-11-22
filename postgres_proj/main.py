from hh_agent import HH_Api
from dbmanager import DB_MANAGER


db_manager = DB_MANAGER('hhrujobs', 1)
db_manager.load_vacancies(15, 'python')
