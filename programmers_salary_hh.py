import requests

from itertools import count
from salary_predictor import fetch_average_salary_hh


def get_vacancies_hh(text, location, page=0):
    link = 'https://api.hh.ru/vacancies'
    payload = {'text': text, 'area': location, 'period': 30, 'only_with_salary': True, 'per_page': 100, 'page': page}
    response = requests.get(link, payload)
    response.raise_for_status()
    return response.json()


def paginator_vacancies_hh(text, location):
    vacancies_list = []
    for page in count():
        page_data = get_vacancies_hh(text, location, page=page)
        if page >= page_data['pages']:
            break
        vacancies_list.extend(page_data['items'])
    return vacancies_list


def get_hh_statistic(language):
    hh_vacancies_list = paginator_vacancies_hh(f'Программист {language}',
                                               location=1  # Moscow
                                               )
    return fetch_average_salary_hh(hh_vacancies_list)


