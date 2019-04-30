import requests

from itertools import count
from salary_predictor import fetch_average_salary_sj


def paginator_vacancies_sj(text, location, secret_key):
    vacancies_list = []
    for page in count():
        page_data = get_vacancies_sj(text, location, secret_key, page=page)
        vacancies_list.extend(page_data['objects'])
        if not page_data['more']:
            break
    return vacancies_list


def get_vacancies_sj(text, location, secret_key, page=0):
    link = 'https://api.superjob.ru/2.0/vacancies'
    headers = {'X-Api-App-Id': secret_key}
    payload = {'keyword': text, 'town': location, 'period': 0, 'catalogues': 48, 'count': 100, 'page': page}
    response = requests.get(link, headers=headers, params=payload)
    response.raise_for_status()
    return response.json()


def get_sj_statistic(language, secret_key):
    sj_vacancies_list = paginator_vacancies_sj(f'Программист {language}',
                                               location=4,  # Moscow
                                               secret_key=secret_key
                                               )
    return fetch_average_salary_sj(sj_vacancies_list)
