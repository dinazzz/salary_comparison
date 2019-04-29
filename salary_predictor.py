def get_predict_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return (salary_from + salary_to) / 2
    elif salary_from:
        return salary_from * 1.2
    elif salary_to:
        return salary_to * 0.8


def get_predict_rub_salary_hh(vacancy):
    salary_info = vacancy['salary']
    if salary_info and salary_info['currency'] == 'RUR':
        return get_predict_salary(salary_info['from'], salary_info['to'])
    else:
        return None


def get_predict_rub_salary_sj(vacancy):
    if vacancy["currency"] == 'rub':
        return get_predict_salary(vacancy['payment_from'], vacancy['payment_to'])
    else:
        return None


def fetch_average_salary_hh(hh_vacancies_list):
    result = {}
    summ = 0
    vacancies_processed = 0
    for vacancy in hh_vacancies_list:
        salary = get_predict_rub_salary_hh(vacancy)
        if salary:
            summ += salary
            vacancies_processed += 1
    result['vacancies_found'] = len(hh_vacancies_list)
    result['vacancies_processed'] = vacancies_processed
    if vacancies_processed == 0:
        result['average_salary'] = 0
    else:
        result['average_salary'] = int(summ / vacancies_processed)
    return result


def fetch_average_salary_sj(sj_vacancies_list):
    result = {}
    summ = 0
    vacancies_processed = 0
    for vacancy in sj_vacancies_list:
        salary = get_predict_rub_salary_sj(vacancy)
        if salary:
            summ += salary
            vacancies_processed += 1
    result['vacancies_found'] = len(sj_vacancies_list)
    result['vacancies_processed'] = vacancies_processed
    if vacancies_processed == 0:
        result['average_salary'] = 0
    else:
        result['average_salary'] = int(summ / vacancies_processed)
    return result
