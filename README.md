# Тестовое задание на позицию разработчика в тестировании (Программист-тестировщик).

Полный текст тестового задания - [здесь](./docs/Тестовое%20задание%20(автотестирование).pdf)

Замечание. Добиться стабильности прохождения тестов близкой к 100% можно добавлением в соответствующие методы ожидания `time.sleep(1)`. Умышленно не стал его добавлять, так как надеюсь найти другое решение.

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
2. Чтобы сохранялась история, перед генерацией отчета, необходимо в папку с результатами прогона скопировать историю
```bash
cp -R ./allure-report/history/ ./allure-results/history
```
3. Генерация готового отчета выполняется командой:
```bash
allure generate --clean
```
4. Сгенерированный отчет будет находиться в папке `allure-report` в файле `index.html`



### Запуск тестов через Docker-compose

Запуск docker-compose с условием его завершения одновременно с сервисом `pytest`
```bash
docker compose up --exit-code-from pytest
```

##### Другие варианты запуска

Запускаем тесты локально, но браузеры запускаются в Grid сетке.

Запуск docker-compose из другой папки и с другим именем:
```bash
docker compose -f docs/docker-compose-hub.yml up --detach
```
или только один контейнер, только для Chrome
``` bash
docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome
```
**ВАЖНО:** в этом варианте запуска тестов необходимо подправить conftest.py в секции для браузера Chrome:
```python
driver = webdriver.Remote(
    command_executor="http://selenium-hub:4444/wd/hub", options=chrome_options
)
```
необходимо в URL изменить `selenium-hub` на `localhost`

### Запуск в GitHub action


trap 'chmod -R 777 allure-results allure-report downloads .pytest_cache' EXIT &&
