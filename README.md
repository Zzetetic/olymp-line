# olymp-line

Дана олимпиадная задача.

```
Задана полоска длиной 2k клеток и шириной в одну клетку. Полоску сгибают пополам так, чтобы правая половинка оказалась под левой. Сгибание продолжают до тех пор, пока сверху находится больше одной клетки. Необходимо пронумеровать клетки таким образом, чтобы после окончания сгибания полосы номера клеток в получившейся колонке были расположены в порядке 1,2,3,4,...,2k.
```

Данная программа ее решает с использованним фреймворка приложений командной строки `cement` и библиотеки интренализации `gettext`.

Программа упаковывается в пакет для распространения.

## Установка

```
$ pip install -r requirements.txt

$ pip install setup.py
```

## Разработка

Этот проект включает набор вспомогательных команд в `Makefile` для автоматизации общих задач разработки.

### Настройка окружени

Следующий текст демонстрирует настройку окружения для разработки и работу с ним:

```
### Создание виртуального окружени `venv` для разработки

$ make venv

$ source env/bin/activate

возможны ошибки из за строки `env/bin/pip install -r requirements-dev.txt` в Makefile` закоментируйте ее с помощью `#` и установите необходимые зависимости в ручную

### Запуск olymp-line приложения командной строки

$ line --help

### Запуск юнит тестов

$ make test
```


### Релиз на PyPi

Перед релизом на PyPi, вы должны, указать реквизиты для работы с PyPI:

**~/.pypirc**:

```
[pypi]
username = YOUR_USERNAME
password = YOUR_PASSWORD
```
Затем используйте вспомогательные команды из `Makefile`:

```
$ make dist

$ make dist-upload
```

## Развертывание

### Docker

Включен базовый `Dockerfile` для сборки и распространения `olymp-line`,
и может быть построен с использованием вспомогательной команды из `Makefile`:

```
$ make docker

$ docker run -it olymp-line --help
```
