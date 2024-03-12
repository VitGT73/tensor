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
6. Генерация отчета Allure:
```bash
allure generate --clean
```
7. Сгенерированный отчет будет находиться в папке `allure-report` в файле `index.html`


Для корректной работы тестов необходимо указать ваш домашний регион в файле `core.config.settings.py`:
```HOME_REGION = 'Ваш регион.'```. Например: ```HOME_REGION = 'Оренбургская обл.'```

При необходимости можно изменить путь к локальной папке для загрузки файлов, сделав соответствующие изменения в модуле `core.config.settings.py`:
```python
   # downloads path
    DOWNLOAD_PATH:str = os.getcwd() + "/downloads"
```
Для ускорения выполнения тестов, а так же для запуска тестов в docker контейнере или CI/CD нужно отключить `headless` режим. Для это нужно раскомментировать следующую строчку `# options.add_argument("--headless")` в файле `conftest.py`

Если при попытке выполнить тесты в Браузере FireFox на Ubuntu выскакивает ошибка: "Your Firefox profile cannot be loaded. It may be missing or inaccessible." То необходимо переустановить FireFox, подробности [тут](https://stackoverflow.com/questions/72405117/selenium-geckodriver-profile-missing-your-firefox-profile-cannot-be-loaded) и [тут](https://www.omgubuntu.co.uk/2022/04/how-to-install-firefox-deb-apt-ubuntu-22-04)

```bash
docker pull selenium/standalone-chrome
```
``` bash
docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome
```

Запуск docker-compose с условием его завершения одновременно с сервисом `pytest`
```bash
docker compose up --exit-code-from pytest
```
Запуск docker-compose из другой папки и с другим именем:
```bash
docker compose -f docs/docker-compose-hub.yml up
```
