import os
import psycopg2
from abc import ABC, abstractclassmethod
from hh_agent import HH_Api

class DB(ABC):
    @abstractclassmethod
    def __init__(self):
        pass

class DB_MANAGER(DB):
    def __init__(self):
        self.conn = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = os.getenv('PASSWD'),
            database = os.getenv('DATABASE')
        )

        self.cur = self.conn.cursor()
        self.cur.execute('select id from vacancies')
        self.vlist = self.cur.fetchall() 
        self.cur.execute('select id from employers')
        self.elist = self.cur.fetchall()

    def check_vacancy_for_repeat(self, vacancy):
        if (int(vacancy['id']), ) in self.vlist:
            return False
        else:
            self.vlist.append((int(vacancy['id'])), )
            return True
        
    def check_employer_for_repeat(self, emp_id):
        if (int(emp_id), ) in self.elist:
            return False
        else:
            self.elist.append((int(emp_id)), )
            return True
    
    def update_employer(self, vacancy):
        if self.check_employer_for_repeat(vacancy['employer']['id']):
            tmp = ()
            tmp = tmp + (int(vacancy['employer']['id']), )
            tmp = tmp + (vacancy['employer']['name'], )
            tmp = tmp + (f'https://hh.ru/employer/{vacancy["employer"]["id"]}', )
            self.cur.execute('insert into employers values(%s, %s, %s)', tmp)


    def load_vacancies(self, count = 10, words = None):
        hh_agent = HH_Api(count)
        vacancies = hh_agent.get_vacancies(words)
        for vacancy in vacancies:
            if vacancy['salary'] != None:
                if vacancy['salary']['currency'] != None:
                    vacancy['currency'] = vacancy['salary']['currency']
                else:
                    vacancy['currency'] = None
            else:
                vacancy['currency'] = None
            if vacancy['salary'] != None:
                if vacancy['salary']['from'] != None:
                    vacancy['salary'] = vacancy['salary']['from']
                else:
                    vacancy['salary'] = vacancy['salary']['to']
            else:
                vacancy['salary'] = 0
            if self.check_vacancy_for_repeat(vacancy):
                tmp = ()
                tmp = tmp + (int(vacancy['id']), )
                tmp = tmp + (vacancy['name'],)
                try:
                    tmp = tmp + (vacancy['snippet']['requirement'].replace('<highlighttext>', '').replace('</highlighttext>', ''), )
                except:
                    tmp = tmp + (None, )
                tmp = tmp + (float(vacancy['salary']),)
                tmp = tmp + (vacancy['currency'],)
                tmp = tmp + (int(vacancy['employer']['id']),)
                tmp = tmp + (vacancy['employer']['name'],)
                tmp = tmp + (f'https://hh.ru/vacancy/{vacancy["id"]}', )
                self.cur.execute('insert into vacancies values(%s, %s, %s, %s, %s, %s, %s, %s)',
                                tmp)
                self.conn.commit()
                self.update_employer(vacancy)
    
    def get_companies_and_vacancies_count(self):
        self.cur.execute('select count(*) from employers')
        ecount = self.cur.fetchone()
        self.cur.execute('select count(*) from vacancies')
        vcount = self.cur.fetchone()
        return [int(ecount[0]), int(vcount[0])]
    
    def get_all_vacancies(self):
        self.cur.execute('select employer_name, name, salary, link from vacancies')
        output = self.cur.fetchall()
        return output
    
    def get_avg_salary(self):
        self.cur.execute('select avg(salary) from vacancies')
        output = self.cur.fetchone()
        return int(output[0])
    
    def get_vacancies_with_higher_salary(self):
        self.cur.execute('select employer_name, name, salary, link from vacancies where salary > (select avg(salary) from vacancies)')
        output = self.cur.fetchall()
        return output
    
    def get_vacancies_with_keyword(self, kwords):
        output = []
        for kword in kwords:
            self.cur.execute(f"select employer_name, name, salary, link from vacancies where name like '%{str(kword).lower()}%' or requirements like '%{str(kword).lower()}%'")
            output.append(self.cur.fetchall())
        return output
    
    def __del__(self):
        self.cur.close()
        self.conn.close()
            