# Приложение отбора кандидатов

## Отбираем кандидатов по заданным критериям

***

***

* Критерии номера
* Критерии навыков


```
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
```

