from os import getenv
from dotenv import load_dotenv
from programmers_salary_hh import get_hh_statistic
from programmers_salary_superjob import get_sj_statistic
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
    hh_stat = {}
    sj_stat = {}
    for language in languages:
        print(f'Загружаются данные по языку {language} с HeadHunter')
        hh_stat[language] = get_hh_statistic(language)
        print(f'Загружаются данные по языку {language} с SuperJob')
        sj_stat[language] = get_sj_statistic(language, secret_key)
    hh_table = make_table('HeadHunter Moscow', hh_stat).table
    sj_table = make_table('SuperJob Moscow', sj_stat).table
    print(hh_table)
    print(sj_table)
