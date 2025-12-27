# Домашнее задание №10: PageObject + Allure

## Структура проекта
10_lesson/
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── calculator_page.py
├── tests/
│   ├── __init__.py
│   ├── test_saucedemo.py    # Firefox
│   └── test_calculator.py   # Chrome
├── conftest.py
├── pytest.ini
├── requirements.txt
├── run_tests.ps1
└── README.md

## Особенности реализации

### Разделение браузеров
- Тест калькулятора запускается через **Chrome**
- Тест интернет-магазина запускается через **Firefox**
- Браузер указывается через параметр командной строки `--browser`

### Запуск тестов

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск теста калькулятора через Chrome
pytest 10_lesson/tests/test_calculator.py --browser=chrome -v

# Запуск теста магазина через Firefox
pytest 10_lesson/tests/test_saucedemo.py --browser=firefox -v

# Запуск через PowerShell скрипт (рекомендуется)
.\run_tests.ps1