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
6. Генерация отчета Allure:
```bash
allure generate --clean
```
7. Сгенерированный отчет будет находиться в папке `allure-report` в файле `index.html`


Для корректной работы тестов необходимо указать ваш домашний регион в файле `.env`:
```HOME_REGION = 'Ваш регион.'```. Например: ```HOME_REGION = 'Оренбургская обл.'```

При необходимости можно изменить путь к локальной папке для загрузки файлов, сделав соответствующие изменения в модуле `links.py`:
```python
   # downloads path
    DOWNLOAD_PATH:str = os.getcwd() + "/downloads"
```
Для ускорения выполнения тестов можно отключить `headless` режим. Для это нужно раскоментировать следующую строчку `# options.add_argument("--headless")` в файле `conftest.py`
