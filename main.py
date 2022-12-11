from flask import Flask
from utils import *


app = Flask(__name__)


@app.route('/')
def home_page():
    """
    Домашняя страница сайта со всеми кандидатами.
    :return: Имя кандидата
             Позиция кандидата
             Навыки через запятую
    """
    candidates = get_all()
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'
    return f'<pre> {result} </pre>'


@app.route('/candidate/<int:pk>')
def get_candidate(pk):
    """
    Данные о кандидатах по pk.
    :param pk:
    :return: Картинку
             Имя кандидата
             Позиция кандидата
             Навыки через запятую
    """
    candidate = get_by_pk(pk)
    if not candidate:
        return'Кандидат не найден'
    result = '<br>'
    result += candidate['name'] + '<br>'
    result += candidate['position'] + '<br>'
    result += candidate['skills'] + '<br>'
    result += '<br>'

    url = candidate['picture']

    return f''' 
        <img src="{url}">
        <pre> {result} </pre>
    '''


@app.route('/candidate/<skill>')
def get_candidates_by_skill(skill):
    """
    Выводит данные кандидата по навыкам.
    :param skill:
    :return: Имя кандидата
             Позиция кандидата
             Навыки через запятую
    """
    candidates = get_by_skill(skill)
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre>'


if __name__ == '__main__':
    app.run(debug=True, port=5001)
