import json
import os.path


def load_candidates():
    """
    Функция загрузит данные из файла.
    :return: json.loads(data).
    """
    filename = 'candidates.json'
    with open(os.path.join(filename), 'rt', encoding='utf-8') as f:
        data = f.read()
        result = json.loads(data)
    return result


def get_all():
    """
    Функция, которая покажет всех кандидатов.
    :return: вернет список словарей всех кандидатов.
    """
    data = load_candidates()
    return data


def get_by_pk(pk):
    """
    Функция, которая вернет кандидата по pk.
    """
    :param pk: pk.
    :return: Кандидат по pk.
    """
    for candidate in get_all():
        if candidate['pk'] == pk:
            return candidate
    return