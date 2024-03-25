# Тестовое задание на позицию разработчика в тестировании (Программист-тестировщик).

Полный текст тестового задания - [здесь](./docs/Тестовое%20задание%20(автотестирование).pdf)


### Установка

1. Cкачать проект в локальную директорию. В текущей директории будет создана папка `tensor`

```bash
git clone https://github.com/VitGT73/tensor.git
```

2. Перейдите в папку с проектом:

```bash
cd tensor
```

3. Создайте виртуальное окружение:
```bash
python -m venv .venv
```
или
```bash
python3 -m venv .venv
```

4. Активируйте виртуальное окружение:
* на Windows:
```bash
.venv\Scripts\activate
```
* На macOS и Linux:
```bash
source .venv/bin/activate
```
4. Установите зависимости. Обязательно убедитесь, что вы перед этим активировали виртуальное окружение:

```bash
pip install -r requirements.txt
```
* !!! ВАЖНО. На момент написания этого Readme. Самая последняя версия pytest==8.0.2. Более поздние, вплоть до 8.1.0 включительно, не корректно работали с Allure. Подробнее - [тут](https://github.com/allure-framework/allure-python/issues/794)

5. Запуск тестов:
```bash
pytest
```

Для корректной работы тестов необходимо указать ваш домашний регион в файле `core.config.settings.py`:
```HOME_REGION = 'Ваш регион.'```. Например: ```HOME_REGION = 'Оренбургская обл.'```

При необходимости можно изменить путь к локальной папке для загрузки файлов, сделав соответствующие изменения в модуле `core.config.settings.py`:
```python
   # downloads path
    DOWNLOAD_PATH:str = os.getcwd() + "/downloads"
```
Для ускорения выполнения тестов, а так же для запуска тестов в docker контейнере или CI/CD нужно отключить `headless` режим. Для это нужно раскомментировать следующую строчку `# options.add_argument("--headless")` в файле `conftest.py`

Если при попытке выполнить тесты в Браузере FireFox на Ubuntu выскакивает ошибка: "Your Firefox profile cannot be loaded. It may be missing or inaccessible." То необходимо переустановить FireFox, подробности [тут](https://stackoverflow.com/questions/72405117/selenium-geckodriver-profile-missing-your-firefox-profile-cannot-be-loaded) и [тут](https://www.omgubuntu.co.uk/2022/04/how-to-install-firefox-deb-apt-ubuntu-22-04)


### Allure отчет

1. Запуск тестов с выгрузкой файлов для allure-отчета:
```bash
pytest --browser=chrome -sv --alluredir=allure-results
```
или для FireFox:
```bash
pytest --browser=firefox -sv --alluredir=allure-results
```
2. Чтобы сохранялась история, перед генерацией отчета, необходимо в папку с результатами прогона скопировать историю из раннее сгенерированного отчета:
```bash
cp -R ./allure-report/history/ ./allure-results/history
```
1. Генерация готового отчета выполняется командой:
```bash
allure generate --clean
```
1. Сгенерированный отчет будет находиться в папке `allure-report` в файле `index.html`



### Запуск тестов через Docker-compose

* Команда `docker compose`(раздельно) используется в новых версиях Докера, в старых, необходимо использовать `docker-compose`(через дефис)

Запуск docker-compose с условием его завершения одновременно с сервисом `pytest`
```bash
docker compose -f docs/docker-compose-hub-pytest.yml up --exit-code-from pytest
```
Будут выполнены тесты использующие сетку Selenium GRID и сформирован Аллюр-отчет в директории проекта.


### Другие варианты запуска docker-compose

##### Запуск docker-compose для Selenium GRID:

```bash
docker compose -f docker-compose-hub.yml up --detach
```
Обратится к браузеру в Selenium GRID можно по адресу `http://selenium-hub:4444/wd/hub`, например:

```python
driver = webdriver.Remote(
    command_executor="http://selenium-hub:4444/wd/hub", options=chrome_options
)
```
Остановка контейнеров:
```bash
docker compose -f docker-compose-hub.yml down
```

### Запуск контейнера с предустановленными Python, Pytest и Allure:

```bash
docker compose -f docker-compose-pytest.yml up --detach
```
Данный контейнер не содержит браузеров FireFox или Chrome поэтому для выполнения тестов нужен запущенный
`docker-compose-hub.yml`.

Выполнить тесты внутри запущенного контейнера для браузера Chrome можно командой:
```bash
docker compose -f docker-compose-pytest.yml exec pytest pytest --browser=chrome -sv --alluredir=allure-results
```
Также доступны другие команды описанные выше:

Копирование истории:
```bash
docker compose -f docker-compose-pytest.yml exec pytest cp -R ./allure-report/history/ ./allure-results/history
```
Генерация отчета. Итоговый проект будет сформирован в папке проекта.
```bash
docker compose -f docker-compose-pytest.yml exec pytest allure generate --clean
```
Контейнеры докер по умолчанию выполняют все команды от имени root, в том числе создают папки с отчетами от его имени. Сбросить права root на эти папки можно следующей командой, которую также можем выполнить из Doker:
```bash
docker compose -f docker-compose-pytest.yml exec pytest /bin/sh -c 'chmod -R 777 allure-results allure-report'
```
* Умышленно не стал изменять В Докере пользователя root на обычного, потому что в противном случае будет не хватать прав при работе в github actions

Остановить контейнер
```bash
docker compose -f docker-compose-pytest.yml down
```

### Запуcк в Github actions

На сайте Github выполняем следующие действия:
- Создаем ветку(branch) - `gh-pages`. Проверяем что по адресу `https://vitgt73.github.io/tensor/` открывается README.md репозитория.
- Генерируем новый токен - [тут](https://github.com/settings/tokens)
- В репозитории, выбираем Settings => Secrets and variables => Actions. Создаем новый секрет GHP_TOKEN (имя можно выбрать любое) и в его значение копируем только, что сгенерированный Токен. Сюда же будем добавлять Логин и Пароль при необходимости.

В локальной папке создаем папку `./.github/workflow`, в ней новый файл - `config.yml`
Ключевые моменты:
Для копирования файлов из ветки `gh-pages` используем скрипт:
```yml
  - name: Checkout (copy) gh-pages repository to GitHub runner
    uses: actions/checkout@v3
    with:
      ref: gh-pages
      path: ./.github/gh-pages
```
Для копирования папки с отчетами `allure-report` в ветку `gh-pages` используем скрипт, в нем мы используем сгенерированный раннее токен `secrets.GHP_TOKEN`:
```yml
    - name: Deploy to Github Pages
      uses: JamesIves/github-pages-deploy-action@4.1.5
      with:
        token: ${{ secrets.GHP_TOKEN }}
        branch: gh-pages
        folder: allure-report
        clean: true
```

Запуск настроен по [кнопке](https://github.com/VitGT73/tensor/actions/workflows/config.yml)
