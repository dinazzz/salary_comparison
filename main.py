from os import getenv
from dotenv import load_dotenv
from programmers_salary_hh import hh_languages_statictic
from programmers_salary_superjob import sj_languages_statictic
from terminaltables import AsciiTable


def make_table(title, vacancies_dict):
    data = [['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']]
    for key, item in vacancies_dict.items():
        row = [key]
        row.extend(item.values())
        data.append(row)
    table = AsciiTable(data, title)
    return table


if __name__ == '__main__':
    load_dotenv()
    secret_key = getenv('SECRET_KEY')
    languages = ['Python', 'Java', 'Ruby', 'JavaScript']
    hh_stat = hh_languages_statictic(languages)
    sj_stat = sj_languages_statictic(languages, secret_key)
    hh_table = make_table('HeadHunter Moscow', hh_stat).table
    sj_table = make_table('SuperJob Moscow', sj_stat).table
    print(hh_table)
    print(sj_table)
