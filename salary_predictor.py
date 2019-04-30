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


def calculate_average_salary(salary_list):
    salary_list_processed = [salary for salary in salary_list if salary is not None]
    vacancies_found = len(salary_list)
    vacancies_processed = len(salary_list_processed)
    average_salary = int(sum(salary_list_processed) / vacancies_processed) if vacancies_processed > 0 else 0
    result = {
        'vacancies_found': vacancies_found,
        'vacancies_processed': vacancies_processed,
        'average_salary': average_salary
    }
    return result


def fetch_average_salary_hh(hh_vacancies_list):
    salary_list = [get_predict_rub_salary_hh(vacancy) for vacancy in hh_vacancies_list]
    return calculate_average_salary(salary_list)


def fetch_average_salary_sj(sj_vacancies_list):
    salary_list = [get_predict_rub_salary_sj(vacancy) for vacancy in sj_vacancies_list]
    return calculate_average_salary(salary_list)
