import json
import os.path


def load_candidates():
    """
    Функция загрузит данные из файла.
    :return: json.loads(data)
    """
    filename = 'candidates.json'
    with open(os.path.join(filename), 'rt', encoding='utf-8') as f:
        data = f.read()
        result = json.loads(data)
    return result


def get_all():
    """
    Функция, которая покажет всех кандидатов.
    :return: вернет список словарей всех кандидатов
    """
    data = load_candidates()
    return data


def get_by_pk(pk):
    """
    Функция, которая вернет кандидата по pk.
    :param pk.
    :return: кандидата по pk.
    """
    for candidate in get_all():
        if candidate['pk'] == pk:
            return candidate
    return


def get_by_skill(skill_name):
    """
    Функция, которая вернет кандидатов по навыку.
    :param skill_name: Наименование навыка.
    :return: Список кандидатов по навыкам.
    """
    candidates = []
    for candidate in load_candidates():
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates
