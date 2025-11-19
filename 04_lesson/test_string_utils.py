import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# ===== ТЕСТЫ ДЛЯ CAPITALIZE =====
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("a", "A"),  # один символ
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Дополнительные тесты для уточнения поведения capitalize
def test_capitalize_mixed_case():
    """Тест на строку со смешанным регистром - документация не ясна """
    result = string_utils.capitalize("SkyPro")
    # Ожидание не определено четко в документации
    assert result == "Skypro"  # Фактическое поведение


def test_capitalize_upper_case():
    """Тест на строку в верхнем регистре"""
    result = string_utils.capitalize("SKYPRO")
    assert result == "Skypro"  # Фактическое поведение


# ===== ТЕСТЫ ДЛЯ TRIM =====
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello", "hello"),
    ("test", "test"),  # без пробелов
    (" one space", "one space"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("    ", ""),  # только пробелы
    ("end space   ", "end space   "),  # пробелы в конце не удаляются
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# ===== ТЕСТЫ ДЛЯ CONTAINS =====
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "y", True),
    ("Hello World", " ", True),
    ("Python", "P", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),  # пустая строка
    ("Hello", "h", False),  # регистрозависимость
    ("Test", "@", False),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# ===== ТЕСТЫ ДЛЯ DELETE_SYMBOL =====
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("Hello World", " ", "HelloWorld"),
    ("aaaa", "a", ""),  # удаление всех символов
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),  # символ не найден
    ("", "a", ""),  # пустая строка
    ("Test", "", "Test"),  # пустой символ для удаления
    ("Hello", "h", "Hello"),  # регистрозависимость
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


# ===== ГРАНИЧНЫЕ СЛУЧАИ =====
def test_contains_with_numbers():
    """Тест на поиск цифр"""
    assert string_utils.contains("123", "1")


def test_delete_symbol_all_occurrences():
    """Тест на удаление всех вхождений буквы"""
    assert string_utils.delete_symbol("облако", "о") == "блак"


def test_trim_preserves_internal_spaces():
    """Тест что внутренние пробелы сохраняются"""
    assert string_utils.trim("   тест    строка   ") == "тест    строка   "
